from django.urls import path
from .views import Login, Logout, homepage, reviews_page, about_page, post_detail

urlpatterns = [
    path('', homepage, name='homepage'), 
    path('reviews/', reviews_page, name='reviews'), 
    path('about/', about_page, name='about'), 
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
