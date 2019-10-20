from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import entry
from .forms import detail


def form_view(request):
    if request.method=='POST':
        form = detail(request.POST or None)
        if form.is_valid():
            form.save()
    form = detail()
    return render(request, 'Bookings.html', {'form' : form})

def home_view(request):
    return render(request, 'Home.html', {})

def about_view(request):
    return render(request, 'About.html', {})

def explore_view(request):
    return render(request, 'Explore.html', {})
