from django.urls import path

from.import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('home',views.home,name='home'),
    path('deposit',views.deposit,name='deposit'),
    path('withdraw',views.withdraw,name='withdraw'),
    path('showinfo',views.showinfo,name='showinfo'),
    path('Select',views.Select,name='Select')
]