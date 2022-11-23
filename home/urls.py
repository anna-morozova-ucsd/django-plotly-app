from django.urls import path
from . import views
from home.dash_apps.finished_apps import simpleexample
from home.dash_apps.finished_apps import anotherexample
from home.dash_apps.finished_apps import thirdexample
from home.dash_apps.finished_apps import hover

urlpatterns = [
    path('', views.home, name='home')
]