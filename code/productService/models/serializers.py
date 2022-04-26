from rest_framework import serializers
from .productModel import Product
print('productserializer works')
class ProductSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=200)
    product_price = serializers.FloatField()
    product_quantity = serializers.IntegerField(required=False, default=1)

    class Meta:
        model = Product
        fields = ('__all__')