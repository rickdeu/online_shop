from django.contrib import admin
from django.urls import path, include
from shop import urls as shop_urls
from cart import urls as cart_urls
from orders import urls as order_urls

#from orders import url as order_urls
from django.conf import settings
from django.conf.urls.static import static

# from shop import urls as shop_ulrs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include(cart_urls, namespace='cart')),
    path('orders/', include(order_urls, namespace='orders')),
    path('', include(shop_urls, namespace='shop')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )