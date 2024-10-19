
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'), 
    path('reviews/', views.reviews_page, name='reviews'), 
    path('about/', views.about_page, name='about'), 
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),

]
