from django.forms import ModelForm, TextInput, CharField
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm


class MessageForm(ModelForm):
    class Meta:
        model = MessageModel
        fields = ['message', "parent"]
        widgets = {
            'message': forms.Textarea(attrs={
                'id': 'name',
                'class': 'form-control'
            })
        }


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': TextInput(attrs={
                "class": "inpt",
                "placeholder": "Username"
            }),
            'password': TextInput(attrs={
                "class": "inpt",
                "placeholder": "Password",
                "type": "password"
            })
        }


class CustomUserForm(UserCreationForm):
    password1 = CharField(
        widget=TextInput(attrs={
            "class": "inpt",
            "placeholder": "Password",
            'type': "password"
        })
    )
    password2 = CharField(
        widget=TextInput(attrs={
            'class': 'inpt',
            'placeholder': 'Confirm your password',
            'type': 'password'
        })
    )

    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'avatar',
                  'bio',
                  'email',
                  'password1',
                  'password2',
                  ]
        widgets = {
            'username': TextInput(attrs={
                'class': 'inpt',
                'placeholder': 'Username',
            }),
            'first_name': TextInput(attrs={
                'class': 'inpt',
                'placeholder': 'First Name',
            }),
            'last_name': TextInput(attrs={
                'class': 'inpt',
                'placeholder': 'Last Name',
            }),
            'bio': TextInput(attrs={
                'class': 'inpt',
                'placeholder': 'Bio',
            }),
            'email': TextInput(attrs={
                'class': 'inpt',
                'placeholder': 'E-mail',
            }),

        }
