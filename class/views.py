from django.shortcuts import render
from .models import Classes


def classvideo(request, video):
    video=video
    videos = Classes.objects.filter(section='Module 1')
    videos1 = Classes.objects.filter(section='Module 2')
    videos2 = Classes.objects.filter(section='Module 3')
    # videos = Classes.objects.all()
    return render(request, "classvideo.html",{'videos': videos,'videos1': videos1,'videos2': videos2,'video' : video})

def classvideo1(request):
    videos = Classes.objects.all()
    return render(request, "classvideo.html",{'videos': videos})

def loginhome(request):
    return render(request, "loginhome.html")