from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path('store/', include('api.v1.store.urls')),
    path('product/', include('api.v1.product.urls')),
]
