from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators

from accounts.models import UserProfile


class RegisterForm(forms.Form):
    phone_number = forms.CharField(label="Phone Number", max_length=10, required=True)
    email = forms.CharField(label="Email", validators=[validators.validate_email], required=True)

    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get('phone_number')

        if len(phone) != 10:
            self.add_error('phone_number', 'โปรดใส่เบอร์ให้ถูกต้อง')