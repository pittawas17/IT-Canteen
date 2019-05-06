from django.conf.urls import url
from django.urls import path
from ordering import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('shop/', views.select_shop, name='select_shop'),
    path('shop/shop_<int:shop_id>/', views.selected, name='selected'),
    path('shop/shop_<int:menu_of>/menu_<int:menu_id>/', views.edit_order, name='edit_order'),
    path('order_status/', views.show_order_status, name='order_status')
]