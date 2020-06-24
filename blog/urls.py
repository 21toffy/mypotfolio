from django.urls import path,include
from django.conf import settings
from  . import views
app_name = 'blog'

urlpatterns = [
    path('posts/', views.PostListView),
]
