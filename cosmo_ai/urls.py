from django.contrib import admin
from django.urls import path
from . import views
from .views import CosmoAi

urlpatterns = [
    path('',views.index,name='index'),
    path('api', CosmoAi.as_view(), name = 'CosmoAi'),
]