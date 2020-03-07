from . import views
from django.urls import path

import others.views
from django.conf.urls import handler404, handler500

app_name='others'

urlpatterns = [

    path('', views.home, name="home"),

    path('contact/',views.contact,name="contact"),

    path('services/',views.services,name="services"),

    path('about/', views.about, name="about"),

    path('email/', views.emailView, name="email"),

    path('about/', views.successView, name="success"),

    path('security/', views.security, name="security"),
    path('seo-optimization/', views.seo_optimization, name="seo-optimization"),
    path('cloud/', views.cloud, name="cloud"),
    path('maintenance/', views.maintenance, name="maintenance"),

]

# handler404 = others.views.handler404
# handler500 = others.views.handler500