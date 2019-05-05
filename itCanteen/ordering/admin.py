from django.contrib import admin

# Register your models here.
from ordering.models import Shop, Menu, Ingredient, Order, OrderItem

admin.site.register(Shop)

admin.site.register(Menu)

admin.site.register(Ingredient)

admin.site.register(Order)

admin.site.register(OrderItem)
