from multiprocessing.managers import Namespace
from django.urls import path
from .views import AlumniRegister
app_name = 'alumni'

urlpatterns = [
    path('',AlumniRegister.as_view(),name='register')
]