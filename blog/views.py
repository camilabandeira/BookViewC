# Django core imports for authentication and user management
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView

# Django utilities for pagination, URL handling, and views
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import View
from django.db.models import Q

# App-specific imports: forms and models
from .forms import (
    LoginForm, ProfileUpdateForm, UserUpdateForm,
    SignupForm, DeleteAccountForm, PostForm, SearchForm
)
from .models import Post, Comment, Profile


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


def signup(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('profile', username=user.username)
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SignupForm()

    return render(request, 'blog/signup.html', {'form': form})


class Login(LoginView):
    template_name = 'blog/login.html'
    form_class = LoginForm


class Logout(LogoutView):
    next_page = 'login'


class DeleteAccountView(LoginRequiredMixin, View):
    form_class = DeleteAccountForm
    template_name = 'blog/delete_account.html'
    login_url = 'login'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = request.user
            logout(request)
            user.delete()
            messages.success(
                request,
                "Your account has been deleted successfully."
            )
            return redirect(reverse_lazy('login'))

        return render(request, self.template_name, {'form': form})


def profile_view(request, username=None):
    user_profile = get_object_or_404(User, username=username)
    user_posts = Post.objects.filter(author=user_profile)
    is_own_profile = (
        request.user.is_authenticated
        and request.user == user_profile
    )

    context = {
        'user_profile': user_profile,
        'user_posts': user_posts,
        'is_own_profile': is_own_profile,
    }
    return render(request, 'blog/profile.html', context)


@login_required(login_url='/login/')
def profile_update(request):
    try:
        user_form = UserUpdateForm(request.POST or None, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST or None, request.FILES or None,
            instance=request.user.profile
        )
    except Profile.DoesNotExist:
        messages.error(request, "Profile not found. Contact support.")
        return redirect('homepage')

    if request.method == 'POST':
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile', username=request.user.username)
        else:
            messages.error(request, 'Please fix the errors below.')

    return render(request, 'blog/profile_update.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })


@login_required(login_url='/login/')
def write_review(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            base_slug = slugify(post.title)
            slug = base_slug
            counter = 1

            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            post.slug = slug
            post.save()
            messages.success(
                request,
                'Your review has been successfully posted!'
            )
            return redirect('post_detail', slug=post.slug)
        else:
            messages.error(
                request,
                'There was an error with your submission. '
                'Please check the form and try again.'
            )
    else:
        form = PostForm()

    return render(request, 'blog/write_review.html', {'form': form})


@login_required(login_url='/login/')
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Post updated successfully."
            )
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})


@login_required(login_url='/login/')
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)
    if request.method == 'POST':
        post.delete()
        messages.success(
            request,
            "Post deleted successfully."
        )
        return redirect('profile', username=request.user.username)
    return render(request, 'blog/confirm_delete_post.html', {'post': post})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.order_by('-created_at')

    paginator = Paginator(comments, 5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST' and request.user.is_authenticated:
        content = request.POST.get('commentText')
        if content:
            Comment.objects.create(
                post=post,
                author=request.user,
                content=content
            )
            messages.success(
                request,
                'Your comment has been posted.'
            )
            return redirect('post_detail', slug=slug)
        else:
            messages.error(request, 'Comment cannot be empty.')

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'page_obj': page_obj,
    })


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.author == request.user:
        post_slug = comment.post.slug
        comment.delete()
        messages.success(request, 'Comment deleted successfully.')
        return redirect('post_detail', slug=post_slug)
    else:
        messages.error(request, "You are not allowed to delete this comment.")
        return redirect('post_detail', slug=comment.post.slug)


def search_posts(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(category__icontains=query) |
            Q(author__username__icontains=query)
        ).distinct()
    else:
        posts = Post.objects.all()

    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/search_results.html', {
        'page_obj': page_obj,
        'query': query
    })
