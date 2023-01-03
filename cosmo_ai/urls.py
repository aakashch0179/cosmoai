from django.contrib import admin
from django.urls import path
from . import views
from .views import WeightPrediction

urlpatterns = [
    path('',views.index,name='index'),
    path('api', WeightPrediction.as_view(), name = 'weight_prediction'),
]