from django.urls import path, include
from . import views


app_name ='account'

urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
]