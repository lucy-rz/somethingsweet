from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Candy, Photo, Order, OrderItem
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

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
    candies = Candy.objects.all()
    return render(request, 'candies/index.html', {
        'candies': candies
    })

def candies_detail(request, candy_id):
    candy = Candy.objects.get(id=candy_id)
    return render (request, 'candies/detail.html', {
        'candy': candy,
    }) 

# def add_to_order(request, candy_id, quantity):
    # Order.objects.get(us)

class CandyCreate(CreateView):
    model = Candy
    fields = ['name', 'country', 'description', 'cost']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

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