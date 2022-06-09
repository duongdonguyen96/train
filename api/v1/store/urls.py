from django.urls import path
from api.v1.store import views

urlpatterns = [
    path('list/', views.get_all, name='store-list'),
    path('detail/<int:store_id>/', views.detail, name='store-detail'),
    path('create/', views.create, name='store-create'),
    path('update/<int:store_id>/', views.update, name='store-update'),
    path('delete/<int:store_id>/', views.delete, name='store-delete'),
]
