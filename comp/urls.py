from django.urls import path
from .import views

urlpatterns=[
    path('home',views.home,name="home"),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('buy/<prod>',views.buy,name="buy"),
    path('orders',views.order,name="order")
]