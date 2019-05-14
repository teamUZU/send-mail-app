from django.urls import path
from . import views

urlpatterns = [
	path('', views.frontpage, name='frontpage'),
	path('client', views.client, name='client'),
	path('user', views.user, name='user'),
    path('createclient', views.createclient, name='createclient'),
    path('createuser', views.createuser, name='createuser'),
    path('editclient/<int:num>', views.editclient, name='editclient'),
    path('edituser/<int:num>', views.edituser, name='edituser'),
    path('sendmailclient/<int:num>', views.sendmailclient, name='sendmailclient'),
    path('sendmailuser/<int:num>', views.sendmailuser, name='sendmailuser'),
    path('broadcastclient', views.broadcastclient, name='broadcastclient'),
    path('broadcastuser', views.broadcastuser, name='broadcastuser'),
]