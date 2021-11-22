from rest_framework import serializers
from ecommerce.models import Product, Order, OrderDetail
from ecommerce.utilities import amount_non_zero, item_repeated, get_product_price, get_usd
from decimal import Decimal


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ['cuantity', 'product']


class OrderSerializer(serializers.ModelSerializer):
    details = OrderDetailSerializer(many=True)
    queryset = Product.objects.all()
    total = serializers.SerializerMethodField()
    total_usd = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'details', 'total', 'total_usd']

    def validate(self, data):
        if not amount_non_zero(data) or item_repeated(data) or not self.stock_non_zero(data):
            raise serializers.ValidationError("Orden de compra invalida")
        if self.context['request'].method == 'POST':
            self.update_stock(data)

        if self.context['request'].method == 'PUT':
            self.rebuild_stock(data)

        return data

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        order = Order.objects.create(**validated_data)
        for detail_data in details_data:
            OrderDetail.objects.create(order=order, **detail_data)
        return order

    def update(self, instance, validated_data):
        details_data = validated_data.pop('details')
        order = instance

        for detail_data in details_data:
            detail = OrderDetail.objects.filter(order=instance, product_id=detail_data['product'])
            if detail.exists():
                detail.update(cuantity=detail_data['cuantity'])
            else:
                product_id = detail_data['product'].id
                OrderDetail.objects.create(order=instance, product_id=product_id, cuantity=detail_data['cuantity'])
                Product.objects.filter(id=product_id).update(stock=Product.objects.get(id=product_id).stock - detail_data['cuantity'])

        return order

    def get_total(self, obj):
        total = 0
        for item in obj.details.all():
            id_product = item.product.id
            cuantity = item.cuantity
            price = get_product_price(Product.objects.all(), id_product)
            total = total + price * cuantity
        return total

    def get_total_usd(self, obj):
        total_price = self.get_total(obj)
        dolar_price = get_usd()
        order_amount_total = total_price / Decimal(dolar_price.replace(',', '.'))
        return order_amount_total.quantize(Decimal('.01'))

    def stock_non_zero(self, data):
        list_to_items = data['details']
        for item in list_to_items:
            product_id = item['product'].id
            stock_actual = Product.objects.get(id=product_id).stock
            print(stock_actual)
            nuevo_stock = stock_actual - item['cuantity']
            if nuevo_stock < 0:
                print('No hay exitencias suficientes para este producto')
                return False

            else:
                return True

    def update_stock(self, data):
        list_to_items = data['details']
        for item in list_to_items:
            product_id = item['product'].id
            stock_actual = Product.objects.get(id=product_id).stock
            nuevo_stock = stock_actual - item['cuantity']
            Product.objects.filter(id=product_id).update(stock=nuevo_stock)
        return None

    def rebuild_stock(self, data):
        list_to_items = data['details']
        for item in list_to_items:
            product_id = item['product'].id
            stock_actual = Product.objects.get(id=product_id).stock
            order_item = OrderDetail.objects.filter(order_id=data['id'], product_id=product_id).first()
            if order_item is not None:
                rebuild_stock = order_item.cuantity + stock_actual
                nuevo_stock = rebuild_stock - item['cuantity']
                Product.objects.filter(id=product_id).update(stock=nuevo_stock)
        return None


