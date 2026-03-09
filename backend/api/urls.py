from django.urls import path

from . import views

urlpatterns=[
    path('', views.api_views, name='api_views'),
    path('create/', views.api_post, name='api_post'),

 
]