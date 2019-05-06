from django.conf.urls import url
from django.urls import path
from ordering import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('shop/', views.select_shop, name='select_shop'),
    path('shop/shop_<int:shop_id>/', views.select_menu, name='selected'),
    path('shop/shop_<int:menu_of>/menu_<int:menu_id>/', views.edit_order, name='edit_order'),
    path('update/shop=<int:shop>menu=<int:menu_id>queue=<int:queue>/', views.update_order, name='update_order'),
    path('remove/shop=<int:shop>menu=<int:menu_id>queue=<int:queue>/', views.remove_order, name='remove_order'),
    path('order_status/', views.show_order_status, name='order_status')
]