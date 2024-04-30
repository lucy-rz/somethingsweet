from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('candies/', views.candies_index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('candies/<int:candy_id>/', views.candies_detail, name='detail'),
    path('candies/create/', views.CandyCreate.as_view(), name='candies_create'),
    path('candies/<int:pk>/update/', views.CandyUpdate.as_view(), name='candies_update'),
    path('candies/<int:pk>/delete/', views.CandyDelete.as_view(), name='candies_delete'),
    path('candies/<int:candy_id>/add_photo', views.add_photo, name='add_photo'),
    path('candies/<int:candy_id>/add_to_order', views.add_to_order, name='add_to_order'),
    path('orders/', views.orders_index, name='orders_index'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('orders/<int:order_id>/complete_order', views.complete_order, name='complete_order')
]