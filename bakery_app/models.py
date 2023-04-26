from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class customer_tbl(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    gender=models.CharField(max_length=150)
    cust_phone=models.CharField(max_length=12)
    cust_image=models.ImageField(upload_to="image/",null=True)

    def __str__(self):
        return self.cust_image

class category_tbl(models.Model):
    category_name=models.CharField(max_length=255)
    cat_image=models.ImageField(upload_to="image/",null=True)

    def __str__(self):
        return self.category_name

class weight_tbl(models.Model):
    weight=models.CharField(max_length=12)

    def __str__(self):
        return self.weight

class product_tbl(models.Model):
    catg=models.ForeignKey(category_tbl,on_delete=models.CASCADE,null=True)
    wgt=models.ForeignKey(weight_tbl,on_delete=models.CASCADE,null=True)
    product_name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    price=models.IntegerField()
    stock=models.IntegerField()
    product_image=models.ImageField(upload_to="image/",null=True)

    def __str__(self):
        return self.product_name,self.price 

class cart_tbl(models.Model):
    cart_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    wght=models.ForeignKey(weight_tbl,on_delete=models.CASCADE,null=True)
    prod=models.ForeignKey(product_tbl,on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField()

    def __str__(self):
        return self.quantity

class multi_image_tbl(models.Model):
    prodt=models.ForeignKey(product_tbl,on_delete=models.CASCADE,null=True)
    multi_image=models.ImageField(upload_to="image/",null=True)

    def __str__(self):
        return self.multi_image  

