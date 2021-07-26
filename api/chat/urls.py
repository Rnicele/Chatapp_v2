from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = format_suffix_patterns([
    path('login/', views.Login.as_view()),
    path('register/', views.Register.as_view()),
    path('users/', views.UserViewSet.as_view({'get': 'list'})),
])
