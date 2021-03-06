import uuid

from django.db import models
from django.urls import reverse
from django.utils import timezone

from products.models import Product
from webshop import settings


class Shipping(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)

    email = models.EmailField()

    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=10)
    home_address = models.CharField(max_length=50)
    name = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse("new-purchase-shipping", kwargs={"uuid": self.pk})

    def get_next_url(self):
        return reverse("new-purchase-payment", kwargs={"uuid": self.pk})


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)

    card_number = models.CharField(max_length=20)
    card_expiry_date = models.DateField()
    card_security_number = models.CharField(max_length=5)
    card_owner_name = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse("new-purchase-payment", kwargs={"uuid": self.pk})


class Purchase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Displayed for both purchase sides

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='purchase_product')
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    purchase_date = models.DateTimeField(default=timezone.now)

    amount = models.IntegerField(default=1, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=10, blank=False)

    # Hidden

    finished = models.BooleanField(default=False)

    shipping = models.ForeignKey(Shipping, on_delete=models.CASCADE, default=None, blank=False, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, default=None, blank=False, null=True)

    def get_accessible_for_list(self):
        return [self.buyer, self.product.seller]

    def get_absolute_url(self):
        return reverse("purchase-details", kwargs={"uuid": self.pk})

    def get_full_price(self):
        return self.amount * self.product.price


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_product')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    addition_date = models.DateTimeField(default=timezone.now)

    amount = models.IntegerField(default=1, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=10, blank=False)

    @staticmethod
    def get_absolute_url():
        return reverse("user-cart")

    def get_full_price(self):
        return self.amount * self.product.price
