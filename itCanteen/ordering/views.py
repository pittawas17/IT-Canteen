from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
import datetime


# Create your views here.
from ordering import forms
from ordering.forms import OrderModelForm
from ordering.models import Shop, OrderItem, Order


@login_required()
def home(request):
    user_type = User.objects.get(id=request.user.id).userprofile.type
    if user_type == "01":
        return customer_main(request)
    else:
        return shop_main(request)


@login_required()
def shop_main(request):
    a = User.objects.get(id=request.user.id).userprofile.shop.shop_name
    return HttpResponse(a)


@login_required()
def customer_main(request):
    a = User.objects.get(id=request.user.id).userprofile.real_first_name
    return HttpResponse(a)


@login_required()
def order(request):
    if request.method == 'POST':
        form = forms.OrderModelForm(request.POST)
        if form.is_valid():
            shop = Shop.objects.get(shop_name='10Pochana')
            user = User.objects.get(id=request.user.id)
            Order.objects.create(
                user=user,
                order_of=user.userprofile.history,
                order_datetime=datetime.datetime.now()
            )
            OrderItem.objects.create(
                menu=form.cleaned_data.get('menu'),
                special_requirement=form.cleaned_data.get('special_requiremenr')
            )
            form.save()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = OrderModelForm()
    return render(request, 'accounts/register.html', {'form': form})