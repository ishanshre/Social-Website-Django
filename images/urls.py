from django.urls import path

from . import views

app_name = 'images'
urlpatterns = [
    path('', views.index, name='index'),

]