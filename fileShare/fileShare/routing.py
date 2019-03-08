from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from share.consumers import ShareConsumer

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                url(r"^$", ShareConsumer),
            ])
        )
    )
})
