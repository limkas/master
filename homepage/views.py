from django.shortcuts import render
from .models import project
# Create your views here.

def home(request):
    return render(request, 'home.html', {'projects' : project})

def project_detail(request):
    return render(request, 'project_detail.html')

def list(request):
    return render(request, 'list.html')