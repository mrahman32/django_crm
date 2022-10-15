from django.urls import path
from . import views
urlpatterns = [
    path('', view=views.home),
    path('products/', view=views.products),
    path('customer/', view=views.customer),
]
