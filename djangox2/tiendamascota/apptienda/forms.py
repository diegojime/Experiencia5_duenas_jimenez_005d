from pyexpat import model
from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Producto
from . models import Cliente
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(forms.ModelForm):

    class Meta: 
        model= Producto
        fields = ['codigo', 'marca', 'categoria']
        labels ={
            'codigo': 'Codigo', 
            'marca': 'Marca', 
            'categoria': 'Categoria', 
        }
        widgets={
            'codigo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese codigo', 
                    'id': 'codigo'
                }
            ), 
            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese marca', 
                    'id': 'marca'
                }
            ), 
            'categoria': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'id': 'Categoria',
                    'placeholder': 'Ingrese categoria', 
                }
            )
        }

class ClienteForm(forms.ModelForm):

    class Meta: 
        model= Cliente
        fields = ['nombre', 'apellido', 'correo', 'rut', 'telefono', 'direccion']
        labels ={
            'nombre': 'Nombre', 
            'apellido': 'Apellido', 
            'correo': 'Correo', 
            'rut': 'rut',
            'telefono': 'Telefono',
            'direccion':'Direccion',
        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese apellido', 
                    'id': 'apellido'
                }
            ), 
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese correo', 
                    'id': 'correo',
                }
            ),
             'rut':forms.TextInput(
                 attrs={
                     'class': 'forms-control',
                     'placeholder': 'ingrese rut',
                     'id': 'rut',
                 }
             )
            
            ,
             'telefono':forms.TextInput(
                 attrs={
                     'class': 'forms-control',
                     'placeholder': 'telefono',
                     'id': 'telefono',
                 }
             )

            ,
             'direccion':forms.TextInput(
                 attrs={
                     'class': 'direccion',
                     'placeholder': 'ingrese direccion',
                     'id': 'direccion',
                 }
             ) 
        }
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User 
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]


        