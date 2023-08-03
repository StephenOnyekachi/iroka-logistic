from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_page/', views.admin_page, name='admin_page'),

    path('users/', views.users, name='users'),
    path('new_user/', views.new_user, name='new_user'),
    path('edit_user/<int:pk>/', views.edit_user, name='edit_user'),
    path('delete_user/<int:pk>/', views.delete_user, name='delete_user'),

    path('edit_item/<int:pk>/', views.edit_item, name='edit_item'),
    path('delete_item/<int:pk>/', views.delete_item, name='delete_item'),
    path('item/', views.item, name='item'),
    path('varify/<int:pk>/', views.varify, name='varify'),

    path('new_item/', views.new_item, name='new_item'),

    path('message/', views.message, name='message'),
    path('delete_message/<int:pk>/', views.delete_message, name='delete_message'),

    path('comment', views.comment, name='comment'),
    path('delete_comment/<int:pk>/', views.delete_comment, name='delete_comment'),
]


