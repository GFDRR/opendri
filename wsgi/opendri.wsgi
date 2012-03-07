import site, os
site.addsitedir('/home/opendri')
os.environ['DJANGO_SETTINGS_MODULE'] = 'opendri.settings'

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
