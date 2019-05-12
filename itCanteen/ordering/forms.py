from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators
from django.forms import ModelForm

from accounts.models import UserProfile
from ordering.models import Shop, OrderItem, Ingredient, Menu


class EditOrderModelForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['special_requirement']


class IngredientModelForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['ingredient_name', 'is_empty']


class MenuModelForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['menu_name', 'is_daily_menu', 'description', 'normal_price', 'special_price', 'menu_type', 'menu_image']