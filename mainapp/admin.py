from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Wishlist)
admin.site.register(WishlishCard)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductBasketCard)
admin.site.register(Basket)
admin.site.register(Order)
