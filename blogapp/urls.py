from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('<int:pk>/', BlogSingleView.as_view(), name='blog_single'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('registration/', registration_user, name='registration'),
]
