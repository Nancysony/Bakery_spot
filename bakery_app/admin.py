from django.contrib import admin
from bakery_app.models import product_tbl,customer_tbl,category_tbl,weight_tbl,cart_tbl,multi_image_tbl
# Register your models here.

admin.site.register(customer_tbl)
admin.site.register(category_tbl)
admin.site.register(weight_tbl)
admin.site.register(product_tbl)
admin.site.register(cart_tbl)
admin.site.register(multi_image_tbl)