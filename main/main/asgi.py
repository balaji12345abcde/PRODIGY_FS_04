import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from chat.rounting import wsPattern

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

application=ProtocolTypeRouter({
    "http":get_asgi_application(),
    "websocket":URLRouter(wsPattern)
})
