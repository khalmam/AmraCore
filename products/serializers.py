from rest_framework import serializers
from .models import Category, Product, BulkPriceTier, ProductVariant

class BulkPriceTierSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulkPriceTier
        fields = ['id', 'min_quantity', 'max_quantity', 'price_per_item']


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['id', 'size', 'color', 'stock']


class ProductSerializer(serializers.ModelSerializer):
    bulk_prices = BulkPriceTierSerializer(many=True, read_only=True)
    variants = ProductVariantSerializer(many=True, read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'category', 'category_name',
            'price', 'currency', 'image', 'is_available',
            'bulk_prices', 'variants', 'created_at'
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
