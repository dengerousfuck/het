from flask import (Blueprint,
                   views,
                   render_template,
                   request,
                   session,
                   url_for,
                    g,
                    abort

                   )
from .forms import SignupForm,SigninForm,AddPostForm,AddCommentForm,AddProjectForm,ForgotpwdForm,UpdatepwdForm
from utils import restful,safeutils,hetcache
from .models import FrontUser,InputInterface
from ..models import BannerModel,BoardModel,PostModel,CommentModel,HighlightPostModel,ReadcountModel
from exts import db
import config,time
from .decorators import login_required
from flask_paginate import Pagination,get_page_parameter
from sqlalchemy.sql import func
import re

bp = Blueprint('front',__name__)


@bp.route('/')
def index():
    board_id = request.args.get('bd',type=int,default=None)
    page = request.args.get(get_page_parameter(), type=int, default=1)
    sort = request.args.get('st',type=int,default=1)
    banners = BannerModel.query.order_by(BannerModel.priority.desc()).limit(4)
    boards = BoardModel.query.all()
    start = (page-1)*config.PER_PAGE
    end = start + config.PER_PAGE
    posts = None
    total = 0
    query_obj = None
    if sort == 1:
        query_obj = PostModel.query.order_by(PostModel.create_time.desc())
    elif sort == 2:
        # 按照加精的时间倒序排序
        query_obj = db.session.query(PostModel).outerjoin(HighlightPostModel).\
            order_by(HighlightPostModel.create_time.desc(),PostModel.create_time.desc())
    elif sort == 3:
        # 按照阅读的数量排序
        # query_obj = PostModel.query.order_by(func.count(ReadcountModel.counts).desc(),PostModel.create_time)
        query_obj = db.session.query(PostModel).outerjoin(ReadcountModel).group_by(PostModel.id).\
                    order_by(func.count(ReadcountModel.counts).desc(),PostModel.create_time)

    elif sort == 4:
        # 按照评论数量排序
        query_obj = db.session.query(PostModel).outerjoin(CommentModel).\
            group_by(PostModel.id).order_by(func.count(CommentModel.id).desc(),PostModel.create_time)


    if board_id:
            query_obj = query_obj.filter(PostModel.board_id== board_id)
            posts = query_obj.slice(start,end)
            total = query_obj.count()

    else:

        posts = query_obj.slice(start,end)
        query_obj.count()

    #
    # print('帖子总数是%s'%total)
    # print('当前是第：%s页'%page)
    count = 0
    read_counts = {}
    answer_counts = {}

    for post in posts:
        read_obj = ReadcountModel.query.filter(ReadcountModel.post_id == post.id).first()
        if not read_obj:
            read_count = 1
        else:
            read_count = read_obj.counts + 1
        answer_count = len(CommentModel.query.filter(CommentModel.post_id == post.id).all())
        answer_counts[post.id] = answer_count
        read_counts[post.id] = read_count
    pagination = Pagination(bs_version=3,page=page,total=total,outer_window=0,inner_window=2)
    context = {
        'banners':banners,
        'boards':boards,
        'posts':posts,
        'pagination':pagination,
        'current_board':board_id,
        'current_sort':sort,
        'answer_counts':answer_counts,
        'read_counts':read_counts

    }
    count += 1
    return render_template('front/front_index.html',**context)


@bp.route('/p/<post_id>/')
def post_detail(post_id):
    post = PostModel.query.get(post_id)
    counts = ReadcountModel.query.filter(ReadcountModel.post_id == post_id).first()
    reads = 0
    if counts:
        reads = counts.counts + 1
        counts.counts += 1
        counts.post_id,counts.counts,counts.post = post_id,reads,post
    else:
        reads = 1
        counts = ReadcountModel(post_id=post.id, counts=reads)
        counts.post = post

    db.session.add(counts)
    db.session.commit()
    if not post:
        abort(404)
    answer_count = len(CommentModel.query.filter(CommentModel.post_id == post_id).all())
    return render_template('front/front_pdetail.html',post=post,answer_count=answer_count,reads=reads)


@bp.route('/aproject/',methods=['POST'])
@login_required
def add_project():
    form = AddProjectForm(request.form)
    if form.validate():
        app_id = form.app_id.data
        name = form.name.data
        interface_name = form.interface_name.data
        interface_url = form.interface_url.data
        parameter_key = form.parameter_key.data
        parameter_value =form.parameter_value.data
        typed = form.typed.data
        methods = form.method.data
        sign = form.sign.data
        domain = form.domain.data
        have_headers = form.have_headers.data
        expected_code = form.expected_code.data
        timestamp = str(int(time.time())*1000)[:13]

        newinterface = InputInterface(app_id=app_id,name=name,interface_name=interface_name,interface_url=interface_url,
                                    parameter_key=parameter_key,parameter_value=parameter_value,typed=typed,methods=methods,
                                    sign=sign,domain=domain,have_headers=have_headers,expected_code=expected_code,
                                      timestamp=timestamp)
        newinterface.author_id = g.front_user.id
        db.session.add(newinterface)
        db.session.commit()
        return restful.success()
    else:
        return restful.params_error(message=form.get_error())



@bp.route('/acomment/',methods=['POST'])
@login_required
def add_comment():
    form = AddCommentForm(request.form)
    if form.validate():
        content = form.content.data
        post_id = form.post_id.data
        post = PostModel.query.get(post_id)
        if post:
            comment = CommentModel(content=content)
            comment.post = post
            comment.author = g.front_user
            db.session.add(comment)
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message='评论的帖子不存在！')
    else:
        return restful.params_error(message=form.get_error())

@bp.route('/apost/',methods=['GET','POST'])
@login_required
def apost():
    if request.method == 'GET':
        boards = BoardModel.query.all()
        return render_template('front/front_apost.html',boards=boards)
    else:
        form = AddPostForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            board_id = form.board_id.data
            board = BoardModel.query.get(board_id)
            if not board:
                return restful.params_error(message='没有这个板块！')
            post = PostModel(title=title,content=content,board_id=board_id)
            post.board = board
            post.author = g.front_user
            db.session.add(post)
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message=form.get_error())


class UpdatepwdView(views.MethodView):
    def get(self):
        return render_template('front/front_updatepwd.html')

    def post(self):
        form = UpdatepwdForm(request.form)
        if form.validate():
            password = form.password1.data
            telephone = updatepwd_telephone
            user = FrontUser.query.filter_by(telephone=telephone).first()
            user.password = password
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message=form.get_error())


class ForgotpwdView(views.MethodView):
    def get(self):
        return render_template('front/front_forgotpwd.html')

    def post(self):
        form = ForgotpwdForm(request.form)
        if form.validate():
            telephone = form.telephone.data
            query_telephone = FrontUser.query.filter_by(telephone=telephone).first()
            if not query_telephone:
                return restful.params_error(message='此号码未注册，请确认后在输入！')
            else:
                global updatepwd_telephone
                updatepwd_telephone = telephone
                return restful.success()
        return restful.params_error(message=form.get_error())


class SignupView(views.MethodView):
    def get(self):
        return_to = request.referrer
        if return_to and return_to != request.url and safeutils.is_safe_url(return_to):
            return render_template('front/front_signup.html',return_to=return_to)
        else:
            return render_template('front/front_signup.html')

    def post(self):
        form = SignupForm(request.form)
        if form.validate():
            telephone = form.telephone.data
            username = form.username.data
            password = form.password1.data
            query_user = FrontUser.query.filter_by(telephone=telephone).first()
            if not query_user:
                user = FrontUser(telephone=telephone,username=username,password=password)
                db.session.add(user)
                db.session.commit()
                return restful.success()
            else:
                return restful.params_error(message='手机号码已注册，请直接登录！')

        else:
            return restful.params_error(message=form.get_error())


class SigninView(views.MethodView):
    def get(self):
        return_to = request.referrer  #返回上一个页面

        if return_to and return_to != request.url \
                and re.search(url_for('front.signup'), return_to) is None\
                and re.search(url_for('front.updatepwd'), return_to) is None\
                and safeutils.is_safe_url(return_to) :

            return render_template('front/front_signin.html',return_to=return_to)
        else:
            return render_template('front/front_signin.html')

    def post(self):
        form = SigninForm(request.form)
        if form.validate():
            telephone = form.telephone.data
            password = form.password.data
            remeber = form.remeber.data
            user = FrontUser.query.filter_by(telephone=telephone).first()
            if user and user.check_password(password):
                session[config.FRONT_USER_ID] = user.id
                if remeber:
                    session.permanent = True
                return restful.success()
            else:
                return restful.params_error(message='手机号码或密码错误！')

        else:
            return restful.params_error(message=form.get_error())


bp.add_url_rule('/signup/',view_func=SignupView.as_view('signup'))
bp.add_url_rule('/signin/',view_func=SigninView.as_view('signin'))
bp.add_url_rule('/forgotpwd/',view_func=ForgotpwdView.as_view('forgotpwd'))
bp.add_url_rule('/updatepwd/',view_func=UpdatepwdView.as_view('updatepwd'))