from django.urls import path
from . import views
from .views import (
    PostCreateView,
    PostListView,
    PostDetail,
    PostDeleteView  ,
    PostUpdateView
)
urlpatterns = [  
    path('', views.home, name="home"),
    path('login/', views.login_user, name='login_user'),
    path('register/', views.register_user, name='register_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('profile/', views.profile, name='profile'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
     path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),  
]
