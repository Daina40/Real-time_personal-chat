from django.urls import path

from chats import views

urlpatterns = [
    path('', views.index, name='home'),
    path('chat/<str:username>/', views.chatpage, name='chat'),
]