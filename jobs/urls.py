from . import views
from django.urls import path


app_name='jobs'

urlpatterns = [
    path('jobs-list/', views.jobslist, name="jobs-list"),
]
