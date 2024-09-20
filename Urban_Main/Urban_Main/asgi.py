"""
ASGI config for Urban_Main project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""


from channels.auth import AuthMiddlewareStack

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Urban_Main.settings')

from Urban_app import consumers

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':AuthMiddlewareStack(URLRouter([path('dashboardSocket/', consumers.DashboardSocket.as_asgi()),]))
    # 'websocket':AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns))
})



