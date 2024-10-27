from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('reviews/', views.reviews_page, name='reviews'),
    path('about/', views.about_page, name='about'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
     path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('profile/update/', views.profile_update, name='profile_update'), 
    path('profile/<str:username>/', views.profile_view, name='profile'),
]
