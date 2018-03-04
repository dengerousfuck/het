from flask import Flask
from apps.cms import bp as cms_bp
from apps.common import bp as common_bp
from apps.front import bp as front_bp
import config
from apps.cms import models
from flask_wtf import CSRFProtect
from exts import db,mail,alidayu
from apps.ueditor import bp as ueditor_bp

def crete_app():
    app = Flask(__name__)
    app.config.from_object(config)

    app.register_blueprint(cms_bp)
    app.register_blueprint(common_bp)
    app.register_blueprint(front_bp)
    app.register_blueprint(ueditor_bp)

    db.init_app(app)
    mail.init_app(app)
    alidayu.init_app(app)
    CSRFProtect(app)
    return app

if __name__ == '__main__':
    app = crete_app()
    app.run(debug=True,host='0.0.0.0')

