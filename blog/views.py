from django.shortcuts import render


def home(request):
    return render(request, 'blog/homepage.html')

def about_page(request):
    return render(request, 'blog/about_page.html')

