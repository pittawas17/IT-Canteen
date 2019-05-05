from django.conf.urls import url
from django.urls import path
from ordering import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('order/', views.order, name='order')
]