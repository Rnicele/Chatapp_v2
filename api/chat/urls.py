from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.Login.as_view()),
    path('register/', views.Register.as_view()),
    path('rooms/', views.RoomList.as_view()),
    path('rooms/<int:pk>', views.RoomDetail.as_view()),
    path('chats/', views.ChatList.as_view()),
    path('chats/<int:pk>', views.ChatDetail.as_view()),
]
