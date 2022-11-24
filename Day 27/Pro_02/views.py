#-*- coding:utf-8 -*-

from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def intro(a):
    return render(a, 'Pro_02/templates/me/intro.html')

def project(a):
    return render(a, 'Pro_02/templates/project/project.html')

def skill(a):
    return render(a, 'Pro_02/templates/skill/skill.html')

def home(a):
    return render(a, 'Pro_02/templates/home/index.html')

def calculator(a):
    return render(a, 'Pro_02/templates/project/toy/Calculator/Calculator.html')