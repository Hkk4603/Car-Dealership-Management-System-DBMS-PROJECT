from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'), 
    path('models/', views.models, name='models'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'), 
    path('logout/', views.logout, name='logout'),
    path('myacc/', views.myacc, name='myacc'),

    #-----------------url patterns for rendering the admin panel-----------------
    #url-> adminpg and user table
    path('adminpg/', views.adminpg, name='adminpg'),
    path('adminpg/addUser', views.addUser, name='addUser'), 
    path('adminpg/delUser', views.delUser, name='delUser'), 
    # path('adminpg/uptUser', views.uptUser, name='uptUser'),   

    #url-> customer table
    path('adminpg/admincus', views.admincus, name='admincus'),
    path('adminpg/addCus', views.addCus, name='addCus'),
    path('adminpg/delCus', views.delCus, name='delCus'),
    path('adminpg/uptCus', views.uptCus, name='uptCus'),

    #url-> carmodels table
    path('adminpg/models', views.carmodels, name='carmodels'), 
    path('adminpg/addCarmodels', views.addCarmodels, name='addCarmodels'), 
    path('adminpg/delCarmodels', views.delCarmodels, name='delCarmodels'), 
    path('adminpg/uptCarmodels', views.uptCarmodels, name='uptCarmodels'), 

    #url-> booking details
    path('adminpg/bookingDetails', views.bookingDetails, name='bookingDetails'), 
    path('adminpg/addBookingDet', views.addBookingDet, name='addBookingDet'), 
    path('adminpg/delBookingDet', views.delBookingDet, name='delBookingDet'), 
    path('adminpg/uptBookingDet', views.uptBookingDet, name='uptBookingDet'),

    #url-> billing
    path('adminpg/billing', views.billing, name='billing'),
    path('adminpg/addBill', views.addBill, name='addBill'),
    path('adminpg/delBill', views.delBill, name='delBill'),
    path('adminpg/uptBill', views.uptBill, name='uptBill'),


    #-----------------url patters for rendering car page-----------------
    path('car/', views.carpg, name='carpg'), 
]
