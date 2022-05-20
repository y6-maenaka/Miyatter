from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path('<uuid:session_id>/',consumers.SessionConsumer.as_asgi()),
]
