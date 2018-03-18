from wtforms import StringField,IntegerField,FileField
from ..forms import BaseForm
from wtforms.validators import Regexp,EqualTo,ValidationError,InputRequired
from utils import hetcache
from flask_wtf.file import FileRequired,FileAllowed


class SignupForm(BaseForm):
    telephone = StringField(validators=[Regexp(r'1[345789]\d{9}',message='请输入正确格式的手机号码')])
    sms_captcha = StringField(validators=[Regexp(r"\w{4}",message='请输入正确格式的短信验证码')])
    username = StringField(validators=[Regexp(r'.{2,20}',message='请输入正确格式的用户名')])
    password1 = StringField(validators=[Regexp(r'[0-9a-zA-Z_\.]{6,20}',message='请输入正确格式的密码！')])
    password2 = StringField(validators=[EqualTo('password1',message='两次输入的密码不一致！')])
    graph_captcha = StringField(validators=[Regexp(r'\w{4}',message='请输入正确格式的图形验证码')])

    def validate_sms_captcha(self,field):
        sms_captcha = field.data
        telephone = self.telephone.data

        sms_captcha_mem = hetcache.get(telephone)
        if not sms_captcha_mem or sms_captcha_mem.lower() != sms_captcha.lower():
            raise ValidationError(message='短信验证码错误！')


    def validate_graph_chaptcha(self,field):
        graph_captcha = field.data

        graph_captcha_mem = hetcache.get(graph_captcha.lower())
        if not graph_captcha_mem:
            raise ValidationError(message='图形验证错误！')


class SigninForm(BaseForm):
    telephone = StringField(validators=[Regexp(r'1[345789]\d{9}', message='请输入正确格式的手机号码')])
    password = StringField(validators=[Regexp(r'[0-9a-zA-Z_\.]{6,20}', message='请输入正确格式的密码！')])
    remeber = StringField()


class ForgotpwdForm(BaseForm):
    telephone = StringField(validators=[Regexp(r'1[345789]\d{9}', message='请输入正确格式的手机号码')])
    sms_captcha = StringField(validators=[Regexp(r"\w{4}", message='请输入正确格式的短信验证码')])

    def validate_sms_captcha(self,field):
        sms_captcha = field.data
        telephone = self.telephone.data

        sms_captcha_mem = hetcache.get(telephone)
        if not sms_captcha_mem or sms_captcha_mem.lower() != sms_captcha.lower():
            raise ValidationError(message='短信验证码错误！')


class UpdatepwdForm(BaseForm):
    password1 = StringField(validators=[Regexp(r'[0-9a-zA-Z_\.]{6,20}', message='请输入正确格式的密码！')])
    password2 = StringField(validators=[EqualTo('password1', message='两次输入的密码不一致！')])


class AddPostForm(BaseForm):
    title = StringField(validators=[InputRequired(message='请输入标题！')])
    content = StringField(validators=[InputRequired(message='请输入内容！')])
    board_id = IntegerField(validators=[InputRequired(message='请输入板块id')])


class AddCommentForm(BaseForm):
    content = StringField(validators=[InputRequired(message='请输入评论内容！')])
    post_id = IntegerField(validators=[InputRequired(message='请输入帖子id')])


class UploadForm(BaseForm):
    avator = FileField(validators=[FileRequired(),FileAllowed(['jpg','png','saz','gif'])])
    desc = StringField(validators=[InputRequired()])

class AddProjectForm(BaseForm):
    app_id = StringField(validators=[InputRequired(message='请输入项目的appid')])
    name = StringField(validators=[InputRequired(message='请输入项目的名字')])
    interface_name = StringField(validators=[InputRequired(message='请输入接口的名字')])
    interface_url = StringField(validators=[InputRequired(message='请输入接口的url')])
    parameter_key = StringField(validators=[InputRequired(message='请输入接口参数的key')])
    parameter_value = StringField(validators=[InputRequired(message='请输入接口参数的value')])
    typed = StringField(validators=[InputRequired(message='请输入请求类型')])
    method = StringField(validators=[InputRequired(message='请输入请求方法')])
    sign = StringField(validators=[InputRequired(message='请输入是否需要签名')])
    domain = StringField(validators=[InputRequired(message='请输入接口域名')])
    have_headers = StringField(validators=[InputRequired(message='请输入是否需要请求头')])
    expected_code = StringField(validators=[InputRequired(message='请输入期望值')])


