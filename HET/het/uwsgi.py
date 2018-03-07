import os

from flask.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zhiliaoketang.settings")

application = get_wsgi_application()