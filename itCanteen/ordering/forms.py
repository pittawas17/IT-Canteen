from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators
from django.forms import ModelForm

from accounts.models import UserProfile
from ordering.models import Shop, OrderItem


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['menu', 'special_requirement']


