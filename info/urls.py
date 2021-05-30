from django.urls import include, path
from . import views
from django_cloud_deployer import runInPaaS, runInFaaS

app_name = 'info'
urlpatterns = [
    runInFaaS(path('help/', include('help.urls'))),
    path('contacts/', views.contacts, name='contacts'),
]
