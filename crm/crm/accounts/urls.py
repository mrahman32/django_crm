from django.urls import path
from . import views
urlpatterns = [
    path('', view=views.home, name="home"),
    path('products/', view=views.products, name="products"),
    path('customer/<str:pk>', view=views.customer, name="customer"),

    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
]
