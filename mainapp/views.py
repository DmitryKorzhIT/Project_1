from django.shortcuts import render
# from .models import *
#
#
# def index(request):
#     """
#     Function of view for the home page.
#     """
#
#     num_products=Product.objects.all().count()
#     num_orders=Order.objects.all().count()
#
#     num_customers=User.objects.filter(role=False).count()
#     num_admins=User.objects.filter(role=True).count()
#
#     return render(
#         request,
#         'index.html',
#         context={'num_products':num_products,'num_orders':num_orders,'num_customers':num_customers,'num_admins':num_admins},
#     )