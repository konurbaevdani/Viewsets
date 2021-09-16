from django.urls import path
from product.views import *


urlpatterns = [
    path('product/', ProductListView.as_view()),
    path('product/<int:pk>/', ProductDetailsView.as_view()),
    path('product/create/', CreateProductView.as_view()),
    path('product/delete/<int:pk>/', DeleteProductView.as_view()),
    path('product/update/<int:pk>/', UpdateProductView.as_view())
]
