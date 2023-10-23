from django.urls import path
from . import api

urlpatterns = [
    path('handleMessage/', api.handleMessage, name='handleMessage'),
]