from django.urls import path
from .views import *

urlpatterns = [
    path('overview', ApiOverview.as_view(), name='api_overview'),
    path('product-list/', ProductList.as_view(), name='product_list'),
    path('create-list/', ProductCreate.as_view(), name='create_list'),
    path('product-detail/<int:id>/', ProductDetail.as_view(), name='product_detail'),
    path('update/<int:id>/', ProductUpdate.as_view(), name='update_product'),
    path('delete/<int:id>/', ProductDelete.as_view(), name='delete_product')
]

