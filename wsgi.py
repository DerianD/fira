# isort:skip
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from django.core.wsgi import get_wsgi_application  # isort:skip
from dj_static import Cling
 
application = Cling(get_wsgi_application())
