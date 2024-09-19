from django.urls import path
from . import consumers

websocket_urlpatterns=[

    path('dashboardSocket/', consumers.DashboardSocket.as_asgi())

]