from django.shortcuts import render, get_object_or_404
from .models import AboutMe

# Create your views here.

def about(request):
    return render(request, 'about/about_me.html',)
