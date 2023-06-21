from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.HomeGet),
    # path('createOrder',views.HomePost),
]