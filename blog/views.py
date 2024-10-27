from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django import forms
from .forms import LoginForm



def homepage(request):
    posts = Post.objects.order_by('-created_on')
    
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/homepage.html', {'page_obj': page_obj})

def about_page(request):
    return render(request, 'blog/about_page.html')

def reviews_page(request):
    posts = Post.objects.order_by('-created_on')

    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/reviews_page.html', {'page_obj': page_obj})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all() 

    if request.method == 'POST' and request.user.is_authenticated:
        content = request.POST.get('commentText')  
        if content:
            Comment.objects.create(post=post, author=request.user, content=content)
            messages.success(request, 'Your comment has been posted.')
            return redirect('post_detail', slug=slug)
        else:
            messages.error(request, 'Comment cannot be empty.')

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})

class Login(LoginView):
    template_name = 'blog/login.html'
    form_class = LoginForm

class Logout(LogoutView):
    next_page = 'login' 