from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
path('index1',views.userindex,name='index1'),
path('index',views.index,name='index'),
path('createbook',views.createbook,name='createbook'),
path('createauthor',views.createauthor,name='createauthor'),
path('searchbook',views.searchbook,name='searchbook'),
path('updatebook/<int:bookid>',views.updatebook,name='updatebook'),
path('deletebook/<int:bookid>',views.deletebook,name='deletebook'),
path('detailbook/<int:bookid>',views.detailbook,name='detailbook'),
path('listbook',views.listbook,name='listbook'),
path('registeration',views.reg_user,name='registeration'),
    path('',views.login,name='login'),
path('newlogin',views.newlogin,name='newlogin'),
    path('logout', views.logout, name='logout'),
]
