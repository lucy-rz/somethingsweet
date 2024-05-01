from django.shortcuts import render, redirect
from .models import Candy, Photo, Order, OrderItem
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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

@login_required
def candies_index(request):
    candies = Candy.objects.all()
    return render(request, 'candies/index.html', {
        'candies': candies
    })

@login_required
def candies_detail(request, candy_id):
    candy = Candy.objects.get(id=candy_id)
    return render (request, 'candies/detail.html', {
        'candy': candy,
    }) 

@login_required
def add_to_order(request, candy_id):
    quantity = request.POST.get('quantity', None)
    if quantity == '':
        quantity = 1
    order = None
    try:
        order = Order.objects.get(user=request.user, current_order=True)
    except Order.DoesNotExist:
        order = Order.objects.create(user=request.user, current_order=True)
    order.candies.add(candy_id, through_defaults={'quantity': quantity})
    print(candy_id, quantity, str(order))
    return candies_index(request)

class CandyCreate(LoginRequiredMixin, CreateView):
    model = Candy
    fields = ['name', 'country', 'description', 'cost']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CandyUpdate(LoginRequiredMixin, UpdateView):
    model = Candy
    fields = ['name', 'country', 'description', 'cost']

class CandyDelete(LoginRequiredMixin, DeleteView):
    model = Candy
    success_url = '/candies'

@login_required
def add_photo(request, candy_id):
    imgurl = request.POST.get('photo-url', None)
    Photo.objects.create(url=imgurl, candy_id=candy_id)
    return redirect('detail', candy_id=candy_id)

@login_required
def orders_index(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/index.html', {
        'orders': orders
    })

@login_required
def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    itemized = zip(order.candies.all(), order.orderitem_set.all())
    order_total = 0
    for item in zip(order.candies.all(), order.orderitem_set.all()):
        total_per_candy_type = item[0].cost * item[1].quantity
        order_total += total_per_candy_type
        print(item)
    return render(request, 'orders/detail.html', {
        'order': order,  
        'itemized': itemized,
        'order_total': order_total,  
    })

@login_required
def complete_order(request, order_id):
    Order.objects.filter(current_order=True, id=order_id).update(current_order=False)
    return redirect('orders_index')

@login_required
def remove_candy(request, order_id, candy_id):
    Order.objects.get(id=order_id).candies.remove(candy_id)
    return redirect('order_detail', order_id=order_id)