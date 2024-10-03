from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin


urlpatterns = [
    path('', views.home, name='blog-home'),  # Homepage
    path('about/', views.about, name='blog-about'),  # about page

    # Autenticazione
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('test/', views.test_view, name='test_view'),  # URL test


    # Post
    path('posts/', views.post_list, name='post_list'),  # post list
    path('post/new/', views.post_create, name='post_create'),  # Creating a new post
    path('post/<slug:slug>/edit/', views.post_update, name='post_update'),  # Update  post
    path('post/<slug:slug>/delete/', views.post_delete, name='post_delete'),  # delete post
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),  # Post detail and comments
]
