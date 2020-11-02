from django.shortcuts import render
from .models import Projects


def landing(request):
    projects = Projects.objects.all()
    return render(request, 'portfolio/landing.html', {'projects': projects})

