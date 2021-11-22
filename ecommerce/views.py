from rest_framework.response import Response
from rest_framework import viewsets, status
from ecommerce.models import Product, Order, OrderDetail
from ecommerce.serializers import ProductSerializer, OrderSerializer, OrderDetailSerializer
from rest_framework.permissions import IsAuthenticated


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]

    def destroy(self, request, pk):
        items = OrderDetail.objects.filter(order_id=pk)
        for item in items:
            product_id = item.product_id
            stock_actual = Product.objects.get(id=product_id).stock
            nuevo_stock = stock_actual + item.cuantity
            Product.objects.filter(id=product_id).update(stock=nuevo_stock)
        #Borra el objeto
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderDetailViewSet(viewsets.ModelViewSet):
    serializer_class = OrderDetailSerializer
    queryset = OrderDetail.objects.all()
