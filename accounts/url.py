from unicodedata import name
from django.urls import path
from . import views



urlpatterns = [
    path('',views.home, name="home"),
    path('products/',views.products, name="products"),
    
    path('customer/<str:pk_test>', views.customer, name="customer"),
    
    path('create_order/<str:pk>',views.createOrder, name="create_order"),
    
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    
    path('user/', views.userPage,name="user"),
    
    
    path('account/', views.accountSettings, name="account"),
    
    
    
    path('products/delete/<str:pk>/', views.product_delete, name='dashboard-products-delete'),
    path('products/edit/<str:pk>/', views.product_edit, name='dashboard-products-edit'),
   
    
    path('login/',views.loginPage, name="login"),
    path('register/',views.register, name="register"),
    path('logout/',views.logoutUser,name='logout'),
    
    path('predict/', views.prediction, name="predict"),
    path('result/', views.result, name="result")
]


