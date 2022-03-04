from django.shortcuts import render


# Create your views here.


def home(request):
    context = {}
    return render(request, 'postings/home.html', context)


def posts(request):
    context = {}
    return render(request, 'postings/posts.html', context)
