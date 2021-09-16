from rest_framework.generics import ListAPIView, RetrieveAPIView, \
    CreateAPIView, UpdateAPIView, DestroyAPIView


from product.models import Product
from product.serializers import ProductListSerializer, ProductDetailSerializer, CreateProductSerializer


class CreateProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class UpdateProductView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer


class DeleteProductView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer


class ProductDetailsView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    # lookup_url_kwarg = 'id'





