from django.urls import path, include
from .views import home # function in views

urlpatterns = [
    path(r'home', home)
]
