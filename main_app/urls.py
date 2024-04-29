from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('candies/', views.candies_index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('candies/<int:candy_id/', views.candies_detail, name='detail'),
    path('candies/create/', views.CandyCreate.as_view(), 'candies_create'),
]