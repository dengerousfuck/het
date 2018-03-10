import os
from PIL import Image,ImageDraw

DEBUG = True
SECRET_KEY = os.urandom(24)


DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'a123456'
HOST ='127.0.0.1'
PORT = '3306'
DATABASE = 'db_mytest'
# PERMANENT_SESSION_LIFETIME =

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False

CMS_USER_ID = 'FSAFDSAFDS'
FRONT_USER_ID = 'FDSFDSAFJDS'

#发送的邮箱的服务器地址
#qq邮箱不支持非加密协议，tls端口是587   ，ssl的端口号是465

MAIL_SERVER='smtp.qq.com'
MAIL_PORT= '587'
MAIL_USE_TLS = True
MAIL_DEBUG=False
MAIL_USERNAME ='390054664@qq.com'
MAIL_PASSWORD = 'geccgojgpknjcadf'
MAIL_DEFAULT_SENDER = '390054664@qq.com'

# 阿里大于相关配置
ALIDAYU_APP_KEY = '23709557'
ALIDAYU_APP_SECRET = 'd9e430e0a96e21c92adacb522a905c4b'
ALIDAYU_SIGN_NAME = '小饭桌应用'
ALIDAYU_TEMPLATE_CODE = 'SMS_68465012'


# UEditor编辑器配置
#UEDITOR_UPLOAD_PATH = os.path.join(os.path.dirname(__file__),'images')
UEDITOR_UPLOAD_TO_QINIU = True
UEDITOR_QINIU_ACCESS_KEY = 'tJLW2rNi_r60-2S_G2urRFzwg74lBarak-U4k9EE'#"M4zCEW4f9XPanbMN-Lb9O0S8j893f0e1ezAohFVL"
UEDITOR_QINIU_SECRET_KEY = 'nVGDI0vihLlEbRQU6EoUz1thNi491aSH0_wS6iMa'#"7BKV7HeEKM3NDJk8_l_C89JI3SMmeUlAIatzl9d4"
UEDITOR_QINIU_BUCKET_NAME = 'denger'#"hyvideo"
UEDITOR_QINIU_DOMAIN = 'http://p4li0s0qf.bkt.clouddn.com/'#"http://7xqenu.com1.z0.glb.clouddn.com/"

# 每一页的帖子数量
PER_PAGE = 4

# celery相关的配置
CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"
CELERY_TASK_SERIALIZER = "json"