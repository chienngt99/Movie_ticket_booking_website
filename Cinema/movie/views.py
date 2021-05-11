from django.shortcuts import render
from .models import *

def HomeView(request):
    posts = MoviePost.objects.all().order_by("-id")
    timeshow = MovieShow.objects.filter().order_by("-id")
    context = {
        'posts': posts,
        'timeshow': timeshow
    }
    return render(request, 'home.html', context)

def MovieDetail(request,id):
    movie_detail = MoviePost.objects.get(id=id)

    context = {
        'movie_detail': movie_detail,
    }

    return render(request, 'movie-detail.html', context)

