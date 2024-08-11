from django.shortcuts import render, get_object_or_404
from .models import Director

def management(request):
    directors = Director.objects.all()
    return render(request, 'info/management.html', {'directors': directors})

def director_detail(request, id):
    director = get_object_or_404(Director, id=id)
    return render(request, 'info/director_detail.html', {'director': director})


def home(request):
    return render(request, 'info/home.html')

def news(request):
    return render(request, 'info/news.html')

# def management(request):
#     return render(request, 'info/management.html')

def activities(request):
    return render(request, 'info/activities.html')

def contacts(request):
    return render(request, 'info/contacts.html')
