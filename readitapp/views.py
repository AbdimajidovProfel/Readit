from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from .forms import *
from blogapp.models import BlogModel


class ReaditView(ListView):
    template_name = 'index.html'
    model = BlogModel
    context_object_name = 'blogs'
    paginate_by = 2


class ContactView(CreateView):
    template_name = 'contact.html'
    model = ContactModel
    form_class = ContactForm
    context_object_name = 'contacts'
    get_absolute_url = 'contact'


