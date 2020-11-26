from django.shortcuts import render
from .models import Project
from blog.models import Blog

# Create your views here.
def home(request):
    project = Project.objects.all()
    return render (request , './templates/protfolio/home.html',{'project' :project})
    