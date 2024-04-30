from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Candy, Photo
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def candies_index(request):
#     candies = Candy.objects.all()
    return render(request, 'candies/index.html', {
        
    })

def candies_detail(request, candy_id):
    candy = Candy.objects.get(id=candy_id)
    return render (candy)

class CandyCreate(CreateView):
    model = Candy
    fields = ['name', 'country', 'description', 'cost']

class CandyUpdate(UpdateView):
    model = Candy
    fields = ['name', 'country', 'description', 'cost']

class CandyDelete(DeleteView):
    model = Candy
    success_url = '/candies'

def add_photo(request, candy_id):
    imgurl = request.POST.get('photo-url', None)
    Photo.objects.create(url=imgurl, candy_id=candy_id)
    return redirect('detail', candy_id=candy_id)