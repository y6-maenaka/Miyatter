"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from session import routing as session_routing
from home import routing as home_routing

from django.urls import path


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':AuthMiddlewareStack(
        URLRouter([
            path('ws_session/',URLRouter(session_routing.websocket_urlpatterns)),
            path('ws_home/',URLRouter(home_routing.websocket_urlpatterns)),
        ])
    )
})



""" Django2.2以前の書き方
import django
get_default_application
django.setup()
"""
