from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

CURRENCY_CHOICES = [
    ('NGN', 'Naira'),
    ('USD', 'US Dollar'),
]

ORDER_TYPE_CHOICES = [
    ('single', 'Single Purchase'),
    ('bulk', 'Bulk Purchase'),
]


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='NGN')
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BulkPriceTier(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='bulk_prices')
    min_quantity = models.PositiveIntegerField()
    max_quantity = models.PositiveIntegerField()
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['min_quantity']

    def __str__(self):
        return f"{self.product.name} ({self.min_quantity}-{self.max_quantity})"


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")
    size = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - {self.size or 'One size'} - {self.color or 'Default'}"
