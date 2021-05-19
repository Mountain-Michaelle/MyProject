from django.urls import path
from . import views                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
""" Defines URL patterns for ll_log"""
app_name = 'll_log'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),    
    # Detail page for a single topic 
    path('topics/<int:topic_id>/', views.topic, name='topic'),                                                                                                 
]