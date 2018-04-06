import os
from PIL import Image,ImageDraw

DEBUG = False
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
PER_PAGE = 20

# celery相关的配置
CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"
CELERY_TASK_SERIALIZER = "json"




#
# import os
#
# # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
#
# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/
#
# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'o%*ivv=n(nb@14t(%8cugo7wg^@eu8%xt$w8butxqi@*@-lelp'
#
# # SECURITY WARNING: don't run with debug turned on in production!
# # DEBUG = False
#
# # 添加域名，或网站的ip地址
# # 以后别人只能通过ALLOWED_HOSTS中的方式进行访问
# ALLOWED_HOSTS = ['123.207.55.21']
#
#
# # Application definition
#
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'news'
# ]
#
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]
#
# ROOT_URLCONF = 'het.urls'
#
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, 'templates')]
#         ,
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
#
# WSGI_APPLICATION = 'het.wsgi.application'
#
#
# # Database
# # https://docs.djangoproject.com/en/1.11/ref/settings/#databases
#
# # DATABASES = {
# #     'default': {
# #         'ENGINE': 'django.db.backends.mysql',
# #         'NAME': 'deploy_demo',
# #         'USER':'root',
# #         'PASSWORD': 'root',
# #         'HOST': '127.0.0.1',
# #         'PORT': '3306'
# #     }
# # }
#
#
# # Password validation
# # https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
#
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

# LANGUAGE_CODE = 'en-us'
#
# TIME_ZONE = 'Asia/Shanghai'   #东八区，防止utc时间少8个小时
#
# USE_I18N = True
#
# USE_L10N = True
#
# USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR,'static_dist') #收集静态文件夹
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR,'static')
# ]

