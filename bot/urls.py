from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.slack_update , name = 'slack_update')
]
