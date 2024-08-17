from django.urls import path
from . import  views 

urlpatterns = [
    path('',views.homepage, name =''),
    path('register', views.register , name='register'),
    path('login', views.login_page, name ='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('user_logout', views.user_logout, name='logout'),
    path('createrecord', views.add_record , name='createrecord'),
    path('updaterecord/<int:pk>', views.update_record, name='updaterecord'),
    path('viewrecord/<int:pk>', views.view_record, name='viewrecord'),
    path('deleterecord/<int:pk>', views.delete_record, name='deleterecord'),
 
]

