from django.conf.urls import url
from django.urls import path
from accounts import views

urlpatterns = [
    path('login_success/', views.login_success, name='login_success'),
    path('register/', views.register, name='register'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]