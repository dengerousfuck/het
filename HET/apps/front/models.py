from exts import db
from werkzeug.security import generate_password_hash,check_password_hash
import shortuuid
import enum
from datetime import datetime

class GenderEnum(enum.Enum):
    MALE = 1
    FEMALE = 2
    SECRET = 3
    UNKNOW = 4


class FrontUser(db.Model):
    __tablename__ = 'front_user'
    id = db.Column(db.String(100),primary_key=True,default=shortuuid.uuid)
    telephone = db.Column(db.String(11),nullable=False,unique=True)
    username = db.Column(db.String(50),nullable=False)
    _password = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(50),unique=True)
    realname = db.Column(db.String(50))
    avatar = db.Column(db.String(100))
    signature = db.Column(db.String(100))
    gender = db.Column(db.Enum(GenderEnum),default=GenderEnum.UNKNOW)
    join_time = db.Column(db.DateTime,default=datetime.now)

    def __init__(self,*args,**kwargs):
        if "password" in kwargs:
            self.password = kwargs.get("password")
            kwargs.pop("password")
        super(FrontUser,self).__init__(*args,**kwargs)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,newpwd):
        self._password = generate_password_hash(newpwd)

    def check_password(self,rawpwd):
        return check_password_hash(self._password,rawpwd)


class InputInterface(db.Model):

    __tablename__ = 'input_interface'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    app_id = db.Column(db.String(10))
    name = db.Column(db.String(20))
    interface_name = db.Column(db.String(100))
    interface_url = db.Column(db.String(1000),nullable=False)
    parameter_key = db.Column(db.String(5000))
    parameter_value = db.Column(db.Text)
    typed = db.Column(db.String(10),nullable=False)
    methods = db.Column(db.String(10),nullable=False)
    expected_code = db.Column(db.String(1000))
    sign = db.Column(db.String(2))
    create_time = db.Column(db.DateTime,default=datetime.now)
    update_time = db.Column(db.DateTime,default=datetime.now)
    timestamp = db.Column(db.String(13))
    domain = db.Column(db.String(500),nullable=False)
    have_headers = db.Column(db.String(2),nullable=False)

    author_id = db.Column(db.String(100),db.ForeignKey('front_user.id'),nullable=False)

    author = db.relationship('FrontUser',backref='interfaces')


class UploadFileForm(db.Model):
    __tablename__ = 'uploadfile'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    desc = db.Column(db.String(100))
    file_url = db.Column(db.String(500))
    file_name = db.Column(db.String(100),nullable=False)

    author_id = db.Column(db.String(100),db.ForeignKey('front_user.id'),nullable=False)

    author = db.relationship('FrontUser',backref='uploadfiles')
