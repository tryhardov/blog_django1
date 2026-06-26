from django.urls import path
from .views import block_list, block_detail, user_page, user_search

urlpatterns = [
    path('', block_list, name='block_list'),
    path('category/<slug:category_slug>/', block_list, name='block_list_by_category'),
    path('<slug:slug>/detail/', block_detail, name='block_detail'),
    path('user/search/', user_search, name='user_search'),
    path('user/<str:username>/', user_page, name='user_page'),
]
