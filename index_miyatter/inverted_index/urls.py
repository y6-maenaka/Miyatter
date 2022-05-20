from django.urls import path
from . import views

app_name = 'inverted_index'

urlpatterns = [
    path('api/inverted_index_control/',views.inverted_index_control,name='inverted_index_control'),
]
