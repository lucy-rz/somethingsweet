from django.shortcuts import render, redirect
# from .models import Candy

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def candies_index(request):
#     candies = Candy.objects.all()
    return render(request, 'candies/index.html', {
        
    })
