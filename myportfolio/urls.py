from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from others import views as myapp_views
from django.conf.urls import handler404, handler500

import others.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobs/',include('jobs.urls', namespace='jobs')),
    path('',include('others.urls', namespace = 'others')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




