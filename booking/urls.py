from django.urls import path
from . import views

urlpatterns = [
    path('', views.rates, name='rates'),
    path('create', views.CreateView.as_view(), name='create'),
]