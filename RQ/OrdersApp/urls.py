from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.HomeGet),
    # path('createOrder',views.HomePost),
    # path('/updateOrderStatus',views.UpdateOrderStatus) # The order was sent to Rakan .
]