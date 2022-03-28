from django.db import models
import uuid
from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField

CATEGORIES= (
    ('Fashion and Clothing','FASHION & CLOTHING'),
    ('Food and Drinks','FOOD & DRINKS'),
    ('Electronics','ELECTRONICS'),
    ('Kids and Babies','KIDS & BABIES'),
    ('Jewelry and Accessories','JEWELRY & ACCESSORIES'),
    ('Home and Decor','HOME & DECOR'),
    ('Arts and Craft','ART & CRAFT'),
    ('Beauty and Wellness','BEAUTY & WELLNESS'),
    ('Pets and Animals','PETS & ANIMALS'),
     ('Books and Publishers','BOOKS & PUBLISHERS'),

)

class Product(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='')
    title = models.CharField(max_length=200)
    image = CloudinaryField('image')
    category  = models.CharField(choices=CATEGORIES, max_length=55)
    price = models.IntegerField(default=0)
    negotiatable = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    view = models.IntegerField(default=0)
    description = models.TextField(max_length=1000)
    location = models.CharField(max_length=200)
    precise_location = models.CharField(max_length=200)
    phone_number = PhoneNumberField(null = True, blank = True)
    negotiatable = models.BooleanField(default=False)

def __str__(self):
        return self.name

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order_details")
    username = models.CharField(max_length=100)
    order_id = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="order_details")
    address_type = models.CharField(max_length=100,choices=[('BILLING', 'Billing'), ('SHIPPING', 'Shipping')])
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.username

class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100)
    total = models.IntegerField(default=0)
    numincart = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="cart")

    def __str__(self):
        return self.username
