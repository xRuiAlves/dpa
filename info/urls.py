from django.urls import include, path

from . import views

app_name = 'info'
urlpatterns = [
    path('help/', include('help.urls')),
    path('contacts/', views.contacts, name='contacts'),
]
