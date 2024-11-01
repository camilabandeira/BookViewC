from django.urls import path
from . import views
from .views import DeleteAccountView

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('reviews/', views.reviews_page, name='reviews'),
    path('about/', views.about_page, name='about'),
    path('write-review/', views.write_review, name='write_review'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<slug:slug>/edit/', views.edit_post, name='edit_post'),
    path('post/<slug:slug>/delete/', views.delete_post, name='delete_post'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('profile/update/', views.profile_update, name='profile_update'), 
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('account/delete/', DeleteAccountView.as_view(), name='delete_account'),
    path('search/', views.search_posts, name='search_posts')
]
