from django.urls import path
from api.v1.product import views

urlpatterns = [
    path('list/', views.get_all, name='song-list'),
    path('detail/<int:product_id>/', views.detail, name='product-detail'),
    path('create/', views.create, name='product-create'),
    path('update/<int:product_id>/', views.update, name='product-update'),
    path('delete/<int:product_id>/', views.delete, name='product-delete'),

]
