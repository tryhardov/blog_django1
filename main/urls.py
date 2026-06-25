from django.urls import path
from .views import block_list

urlpatterns = [
    path('', block_list, name='block_list'),
    path('category/<slug:category_slug>/', block_list, name='block_list_by_category'),
    path('user/<str:username>/', block_list, name='block_list_by_username')
]
