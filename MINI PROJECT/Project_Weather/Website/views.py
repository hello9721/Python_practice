from django.shortcuts import render
from .models import *

def home(req):

    lst = Srtncst.objects.all()
    context = {'list' : lst}

    return render(req, 'home/index.html', context)