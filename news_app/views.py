from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import News
from .forms import NewsForm
# Create your views here.

def home(request):
    news = News.objects.all()
    return render(request, 'pages/index.html',{'news': news})

def about_us(request):
    return render(request, 'pages/about_us.html')

def create_new(request):
    form = NewsForm(request.POST or None, request.FILES or None )
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'news/create_new.html', {'form':form})

def edit_new(request, id):
    news = News.objects.get(id=id)
    form = NewsForm(request.POST or None, request.FILES or None, instance=news)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('home')
    return render(request, 'news/edit_new.html', {'form': form})

def delete_news(request, id):
    news = News.objects.get(id=id)
    news.delete()
    return redirect('home')

def news_detail(request, id):
    news = News.objects.get(id=id)

    return render(request, 'news/news_detail.html', {'news': news})