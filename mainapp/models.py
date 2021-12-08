from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = get_user_model()

# Create your models here.

#*********************
# 1.User
# 2.Customer
# 3.ProductCategory
# 4.Product
# 5.Wishlist
# 6.WishlistCard
# 7.Basket
# 8.ProductBasketCard
# 9.Order
#*********************


class User(models.Model):

    user_id = models.AutoField(primary_key=True, verbose_name='User id', default=1000000000000)
    role = models.BooleanField(verbose_name='Role')  # False:user, True:admin
    name = models.CharField(max_length=255, verbose_name='Name')
    email = models.EmailField(max_length=255, verbose_name='Email')
    password = models.CharField(max_length=255, verbose_name='Password')
    # slug = models.SlugField(unique=True)

    def __str__(self):
        return self.user_id


class Customer(models.Model):

    customer_id = models.AutoField(primary_key=True, verbose_name='Customer id', default=2000000000000)
    user_id = models.OneToOneField(User, verbose_name='User id', on_delete=models.CASCADE)
    # slug = models.SlugField(unique=True)

    def __str__(self):
        return self.customer_id


class ProductCategory(models.Model):

    category_id = models.AutoField(primary_key=True, verbose_name='Category id', default=8000000000000)
    category_name = models.CharField(max_length=255, verbose_name='Category name', default='')
    # slug = models.SlugField(unique=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):

    # class Meta:
    #     abstract = True

    product_id = models.AutoField(primary_key=True, verbose_name='Product id', default=7000000000000)
    image = models.ImageField(verbose_name='Image')
    title = models.CharField(max_length=255, verbose_name='Title')
    category_id = models.ForeignKey(ProductCategory, verbose_name='Category id', null=True, on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Description', null=True)
    basket_card_description = models.CharField(max_length=350, verbose_name='Basket card description', null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Price')
    # slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Wishlist(models.Model):

    wishlist_id = models.AutoField(primary_key=True, verbose_name='Wishlist id', default=3000000000000)
    customer_id = models.OneToOneField(Customer, verbose_name='Customer id', on_delete=models.CASCADE)
    # slug = models.SlugField(unique=True)

    def __str__(self):
        return self.wishlist_id


class WishlishCard(models.Model):

    wishlist_id = models.ForeignKey(Wishlist, verbose_name='Wishlist id', on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, verbose_name='Product id', on_delete=models.CASCADE)
    # slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.wishlist_id} {self.product_id}'


class Basket(models.Model):

    basket_id = models.AutoField(primary_key=True, verbose_name='Basket id', default=5000000000000)
    customer_id = models.ForeignKey(Customer, verbose_name='Customer id', on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Total price')
    # slug = models.SlugField(unique=True)

    def __str__(self):
        return self.total_price


class ProductBasketCard(models.Model):

    product_basket_card_id = models.AutoField(primary_key=True, verbose_name='Product basket card id', default=6000000000000)
    product_id = models.ForeignKey(Product, verbose_name='Product id', on_delete=models.CASCADE)
    basket_id = models.ForeignKey(Basket, verbose_name='Basket id', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, verbose_name='Quantity')
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey('content_type', 'object_id')
    # slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.product_id} {self.basket_id}'


class Order(models.Model):

    order_id = models.AutoField(primary_key=True, verbose_name='Order id', default=4000000000000)
    basket_id = models.ForeignKey(Basket, verbose_name='Basket id', on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, verbose_name='Customer id', on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Total price')
    comment = models.TextField(verbose_name='Comment', null=True)
    # slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.order_id} {self.total_price}'


