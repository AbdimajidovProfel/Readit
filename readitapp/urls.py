from django.urls import path
from .views import *


urlpatterns = [
    path('', ReaditView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
]
