from django.forms import ModelForm
from .models import *
from django import forms


class ContactForm(ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                "class": 'form-control',
                'placeholder': "Your Name",
            }),
            'phone': forms.TextInput(attrs={
                "class": 'form-control',
                'placeholder': "Your Phone",
            }),
            'email': forms.TextInput(attrs={
                "class": 'form-control',
                'placeholder': "Your Email",
            }),
            'subject': forms.TextInput(attrs={
                "class": 'form-control',
                'placeholder': "Subject",
            }),
            'message': forms.Textarea(attrs={
                "class": 'form-control',
                'placeholder': "Message",
            }),
        }


