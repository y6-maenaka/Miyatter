from django.urls import path
from . import views

app_name = 'session_index'

urlpatterns = [
    path('api/',views.session_index,name='session_index'),
]
