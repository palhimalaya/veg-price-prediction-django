from dataclasses import field
from pyexpat import model
from urllib import request
from django.forms import ModelForm
from .models import Customer, Order, Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from .models import Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'



class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']
        
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
                
class PredictForm(forms.Form):
    
    day = forms.CharField()
    month = forms.CharField()
    year = forms.CharField()