from django.urls import path
from . import views

urlpatterns=[
    path('', views.user_list, name='user_list'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('create/', views.user_create, name='user_create'), 
    path('update/<int:pk>/', views.user_update, name ='user_update'),
    path('delete/<int:pk>/', views.user_delete, name='user_delete')
]
