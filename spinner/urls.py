from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('member',views.member,name='member'),
    path('prashant',views.prashant,name='prashant'),
    path('member2',views.member2,name='member2'),
    path('member3',views.member3,name='member3'),
    path('history',views.history,name='history'),
    path('services',views.services,name='services'),
]
