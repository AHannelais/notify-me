from channels.routing import ProtocolTypeRouter, URLRouter
from backend.notifications.routing import websockets
application = ProtocolTypeRouter({
    "websocket": websockets,
})
