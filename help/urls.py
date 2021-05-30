from django.urls import path
from . import views
from django_cloud_deployer import runInPaaS, runInFaaS

app_name = 'help'
urlpatterns = [
    path('', views.help, name='help'),
    path('shopping/', views.shopping_help, name='shopping_help'),
    path('billing/', views.billing_help, name='billing_help'),
    path('returns/', views.returns_help, name='returns_help'),
]
