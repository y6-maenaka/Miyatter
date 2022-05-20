from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('',consumers.HomeConsumer.as_asgi()),
]
