from channels.routing import ProtocolTypeRouter, URLRouter
from backend.notifications.routing import websockets
from backend.notifications.middlewares import TokenAuthMiddlewareStack
application = ProtocolTypeRouter({
    "websocket": TokenAuthMiddlewareStack(websockets),
})
