from flask import Blueprint,views,render_template,request,session,redirect,url_for,g,jsonify
from .forms import LoginForm,ResetpwdForm,ResetEmailForm,AddBannerForm,UpdateBannerForm,AddBoardForm,UpdateBoardForm
from .models import CMSUser,CMSPersmisson
from .decorators import login_required,permission_required
from ..models import BannerModel,BoardModel,PostModel,HighlightPostModel
import config
from exts import db,mail
from utils import restful,hetcache
from flask_mail import Message
import string
import random
from tasks import send_mail

bp = Blueprint('cms',__name__,url_prefix='/cms')


@bp.route('/')
@login_required
def index():
    return render_template('cms/cms_index.html')


@bp.route('/profile/')
@login_required
def profile():
    return render_template('cms/cms_profile.html')


@bp.route('/loginout/')
@login_required
def loginout():
    del session[config.CMS_USER_ID] #session.clear()
    return redirect(url_for('cms.login'))


@bp.route('/email_captcha/')
def email_captcha():
    email = request.args.get('email')
    if not email:
        return restful.params_error('请传递邮箱参数！')
    source = list(string.ascii_letters)
    source.extend(map(lambda x :str(x),range(10)))
    captcha = ''.join(random.sample(source,6))  #返回的是列表
    # message = Message('python后台邮箱验证码',recipients=[email],body='您的验证码是：%s'%captcha)
    #
    # try:
    #     mail.send(message)
    # except:
    #     return restful.server_error()
    send_mail.delay('python后台邮箱验证码', [email], '您的验证码是：%s' % captcha)
    hetcache.set(email,captcha)

    return restful.success()



@bp.route('/email/')
def send_email():
    message = Message('测试邮件发送',recipients=['153531611@qq.com'],body='小伙子你好帅呀')
    mail.send(message)
    return 'successful'


@bp.route('/posts/')
@login_required
@permission_required(CMSPersmisson.POSTER)
def posts():
    context={
        'posts':PostModel.query.all()
    }
    return render_template('cms/cms_posts.html',**context)


@bp.route('/hpost/',methods=['POST'])
@login_required
@permission_required(CMSPersmisson.POSTER)
def hpost():
    post_id = request.form.get('post_id')
    if not post_id:
        return restful.params_error(message='请传入帖子id')
    post = PostModel.query.get(post_id)
    if not post:
        return restful.params_error('没有这篇帖子！')
    highlight = HighlightPostModel()
    highlight.post = post
    db.session.add(highlight)
    db.session.commit()
    return restful.success()


@bp.route('/uhpost/',methods=['POST'])
@login_required
@permission_required(CMSPersmisson.POSTER)
def uhpost():
    post_id = request.form.get('post_id')
    if not post_id:
        return restful.params_error(message='请传入帖子id')
    post = PostModel.query.get(post_id)
    if not post:
        return restful.params_error('没有这篇帖子！')
    highlight = HighlightPostModel.query.filter_by(post_id=post_id).first()
    db.session.delete(highlight)
    db.session.commit()
    return restful.success()


@bp.route('/comments/')
@login_required
@permission_required(CMSPersmisson.COMMENTER)
def comments():
    return render_template('cms/cms_comments.html')


@bp.route('/boards/')
@login_required
@permission_required(CMSPersmisson.BOARDER)
def boards():
    board_models = BoardModel.query.all()
    context = {
        'boards':board_models
    }
    return render_template('cms/cms_boards.html',**context)


@bp.route('/fusers/')
@login_required
@permission_required(CMSPersmisson.FRONTUSER)
def fusers():
    return render_template('cms/cms_fusers.html')


@bp.route('/cusers/')
@login_required
@permission_required(CMSPersmisson.CMSUSER)
def cusers():
    return render_template('cms/cms_cusers.html')


@bp.route('/croles/')
@login_required
@permission_required(CMSPersmisson.ALL_PERMISSION)
def croles():
    return render_template('cms/cms_croles.html')


@bp.route('/cinterfaces/')
@login_required
@permission_required(CMSPersmisson.ALL_PERMISSION)
def cinterfaces():
    return render_template('cms/cms_interfaces.html')

@bp.route('/banners/')
@login_required
def banners():
    banners = BannerModel.query.order_by(BannerModel.priority.desc()).all()
    return render_template('cms/cms_banners.html',banners=banners)


@bp.route('/abanner/',methods=['POST'])
@login_required
def abanner():
    form = AddBannerForm(request.form)
    if form.validate():
        name = form.name.data
        image_url = form.image_url.data
        link_url = form.link_url.data
        priority = form.priority.data
        banner = BannerModel(name=name,image_url=image_url,link_url=link_url,priority=priority)
        db.session.add(banner)
        db.session.commit()
        return restful.success()

    else:
        return restful.params_error(message=form.get_error())


@bp.route('/ubanner/',methods=['POST'])
@login_required
def ubanner():
    form = UpdateBannerForm(request.form)
    if form.validate():
        banner_id = form.banner_id.data
        name = form.name.data
        image_url = form.image_url.data
        link_url = form.link_url.data
        priority = form.priority.data
        banner = BannerModel.query.get(banner_id)
        if banner:
            banner.name = name
            banner.image_url = image_url
            banner.link_url = link_url
            banner.priority = priority
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message='没有这个轮播图！')


    else:
        return restful.params_error(message=form.get_error())


@bp.route('/dbanner/',methods=['POST'])
@login_required
def dbanner():
    banner_id = request.form.get('banner_id')
    if not banner_id:
        return restful.params_error(message='请传入轮播入id')
    banner = BannerModel.query.get(banner_id)
    if not banner:
        return restful.params_error(message='没有这个轮播图！')
    db.session.delete(banner)
    db.session.commit()
    return restful.success()

@bp.route('/aboard/',methods=['POST'])
@login_required
@permission_required(CMSPersmisson.BOARDER)
def aboard():
    form = AddBoardForm(request.form)
    if form.validate():
        name = form.name.data
        board = BoardModel(name=name)
        db.session.add(board)
        db.session.commit()
        return restful.success()
    else:
        return restful.params_error(message=form.get_error())


@bp.route('/uboard/',methods=['POST'])
@login_required
@permission_required(CMSPersmisson.BOARDER)
def uboard():
    form = UpdateBoardForm(request.form)
    if form.validate():
        board_id = form.board_id.data
        name = form.name.data
        board = BoardModel.query.get(board_id)
        if board:
            board.name = name
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message='没有这个板块')
    else:
        return restful.params_error(message=form.get_error())


@bp.route('/dboard/',methods=['POST'])
@login_required
@permission_required(CMSPersmisson.BOARDER)
def dboard():
    board_id = request.form.get('board_id')
    if not board_id:
        return restful.params_error(message='请传入板块id')
    board = BoardModel.query.get(board_id)
    if not board:
        return restful.params_error(message='没有这个板块！')
    db.session.delete(board)
    db.session.commit()
    return restful.success()


class LoginView(views.MethodView):
    def get(self,message = None):
        return render_template('cms/cms_login.html',message=message)

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = CMSUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[config.CMS_USER_ID] = user.id
                if remember:
                    #如果设置session.permanent=True,那么过期时间是31天
                    session.permanent = True
                return redirect(url_for('cms.index'))
            else:
                return  self.get(message='邮箱或者密码错误')

        else:
            message = form.get_error()
            return self.get(message=message)

class ResetPwdView(views.MethodView):
    decorators = [login_required]
    def get(self):
        return render_template('cms/cms_resetpwd.html')
    def post(self):
        form = ResetpwdForm(request.form)
        if form.validate():
            oldpwd = form.oldpwd.data
            newpwd = form.newpwd.data
            user = g.cms_user
            if user.check_password(oldpwd):
                user.password = newpwd
                db.session.commit()
                return restful.success()
            else:
                return restful.params_error('旧密码错误！')
        else:
            return restful.params_error(form.get_error())

class ResetEmailView(views.MethodView):

    decorators = [login_required]

    def get(self):
        return render_template('cms/cms_resetemail.html')

    def post(self):

        form = ResetEmailForm(request.form)
        if form.validate():
            email = form.email.data
            g.cms_user.email = email
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(form.get_error())


bp.add_url_rule('/resetemail/',view_func=ResetEmailView.as_view('resetemail'))
bp.add_url_rule('/login/',view_func=LoginView.as_view('login'))
bp.add_url_rule('/resetpwd/',view_func=ResetPwdView.as_view('resetpwd'))