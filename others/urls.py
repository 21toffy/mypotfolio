from . import views
from django.urls import path

app_name='others'

urlpatterns = [

    path('', views.home, name="home"),

    path('contact/',views.contact,name="contact"),

    path('services/',views.services,name="services"),

    path('about/', views.about, name="about"),

    path('email/', views.emailView, name="email"),

    path('about/', views.successView, name="success"),
]
