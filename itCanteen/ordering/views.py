from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect
import datetime

# Create your views here.
from ordering import forms
from ordering.forms import EditOrderModelForm
from ordering.models import Shop, OrderItem, Order, Menu, ShopQueue


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
def select_shop(request):
    shop_list = Shop.objects.all()
    context = {
        'shop_list': shop_list
    }
    return render(request, template_name='ordering/select_shop.html', context=context)


@login_required()
def select_menu(request, shop_id):
    shop = Shop.objects.get(id=shop_id)
    menu_list = Menu.objects.filter(menu_of_id=shop_id).filter(is_daily_menu=True)
    context = {
        'shop': shop,
        'menu_list': menu_list
    }
    return render(request, template_name="ordering/select_menu.html", context=context)


@login_required()
def edit_order(request, menu_of, menu_id):
    shop = Shop.objects.get(id=menu_of)
    menu = Menu.objects.get(id=menu_id)
    user = User.objects.get(id=request.user.id)
    shop_queue = shop.shopqueue
    if request.method == 'POST':
        form = forms.EditOrderModelForm(request.POST)
        if form.is_valid():
            order_datetime = datetime.datetime.now()
            add_queue(shop)
            if menu.special_price:
                if request.POST.get('size') == "01":
                    price = menu.normal_price
                else:
                    price = menu.special_price
            else:
                price = menu.normal_price
            OrderItem.objects.create(
                menu=menu,
                queue=shop_queue,
                order=user.userprofile.order,
                order_datetime=order_datetime,
                this_queue=shop_queue.current_queue,
                special_requirement=form.cleaned_data.get('special_requirement'),
                price=price
            )
            order_item = OrderItem.objects.get(menu=menu, queue=shop_queue, order=user.userprofile.order, order_datetime=order_datetime)
            order_item.wait = order_item.this_queue - shop_queue.last_queue
            order_item.save()
            return redirect('order_status')
    else:
        form = EditOrderModelForm()
    context = {
        'shop': shop,
        'menu': menu,
        'forms': form
    }
    return render(request, 'ordering/edit_order.html', context=context)


def add_queue(shop):
    shop_queue = shop.shopqueue
    shop_queue.current_queue += 1
    shop_queue.queue = shop_queue.current_queue - shop_queue.last_queue
    shop_queue.save()


def remove_queue(shop, rem_queue):
    shop_queue = shop.shopqueue
    OrderItem.objects.filter(queue=shop_queue, this_queue=rem_queue).delete()
    for i in OrderItem.objects.filter(queue=shop_queue):
        if i.this_queue > rem_queue:
            i.this_queue -= 1
            i.save()
    shop_queue.current_queue -= 1
    shop_queue.queue = shop_queue.current_queue - shop_queue.last_queue
    shop_queue.save()
    update_wait(shop)


def queue_done(shop):
    shop_queue = shop.shopqueue
    shop_queue.last_queue += 1
    shop_queue.queue = shop_queue.current_queue - shop_queue.last_queue
    shop_queue.save()
    update_wait(shop)


def update_wait(shop):
    shop_queue = shop.shopqueue
    order_in_shop = OrderItem.objects.filter(queue=shop_queue)
    for i in order_in_shop:
        i.wait = i.this_queue - shop_queue.last_queue
        i.save()
    shop_queue.save()


@login_required()
def show_order_status(request):
    user = User.objects.get(id=request.user.id).userprofile
    order = user.order
    order_item = OrderItem.objects.filter(order=order)
    order.total_price = (order_item.aggregate(Sum('price')))['price__sum']
    order.save()
    context = {
        'order': order,
        'order_item': order_item,
    }
    return render(request, 'ordering/order_status.html', context=context)


@login_required()
def update_order(request, shop, menu_id, queue):
    shop = Shop.objects.get(id=shop)
    menu = Menu.objects.get(id=menu_id)
    user = User.objects.get(id=request.user.id)
    shop_queue = shop.shopqueue
    if request.method == 'POST':
        form = forms.EditOrderModelForm(request.POST)
        if form.is_valid():
            add_queue(shop)
            if menu.special_price:
                if request.POST.get('size') == "01":
                    price = menu.normal_price
                else:
                    price = menu.special_price
            else:
                price = menu.normal_price
            order_item = OrderItem.objects.get(this_queue=queue)
            order_item.special_requirement = form.cleaned_data.get('special_requirement')
            order_item.price = price
            order_item.wait = order_item.this_queue - shop_queue.last_queue
            order_item.save()
            return redirect('order_status')
    else:
        form = EditOrderModelForm()
    context = {
        'shop': shop,
        'menu': menu,
        'forms': form
    }
    return render(request, 'ordering/edit_order.html', context=context)


@login_required()
def remove_order(request, shop, menu_id, queue):
    shop = Shop.objects.get(id=shop)
    menu = Menu.objects.get(id=menu_id)
    user = User.objects.get(id=request.user.id)
    shop_queue = shop.shopqueue
    remove_queue(shop, queue)
    return redirect('order_status')
