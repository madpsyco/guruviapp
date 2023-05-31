from django.shortcuts import render
from .models import Course
def index(request):
    mydata = Course.objects.all()
    return render(request, "index.html",{'mymembers': mydata
                                         })

