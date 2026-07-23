from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeSimView.as_view(),name='home')
]