from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request, 'main_app/index.html')

def search(request):
    return render(request, 'main_app/search.html')

def news(request):
    return render(request, 'main_app/news.html')
