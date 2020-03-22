"""
WSGI config for myportfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""
import os
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application
project_folder = os.path.expanduser('~/mypotfolio')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myportfolio.settings")

application = get_wsgi_application()
