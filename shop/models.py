from django.db import models
# from accounts.models import *
from payment.models import Discount

from time import gmtime, strftime
from django.utils.text import slugify
from taggit.managers import TaggableManager

# from unidecode import unidecode
# Create your models here.

class Inventory(models.Model):
    quantity = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField()
    

class Category(models.Model):
    slug = models.SlugField(allow_unicode=True)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField()
    
    
    def __str__(self):
        return self.name 
    
class Brand(models.Model):
    slug = models.SlugField(allow_unicode= True)
    name = models.CharField(max_length=100)
    logo = models.ImageField(
        upload_to='static/images/logos/' ,
        default='no-image.jpg' ,
        null=True ,blank=True  ,
        width_field='imagewidth'  ,
        height_field='imageheight' ,
    )
    imagewidth = models.PositiveIntegerField(editable = False, default = 50)
    imageheight = models.PositiveIntegerField(editable = False, default = 50)
    
    description = models.TextField()
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField() 

    class Meta: 
        verbose_name_plural= "Brand"

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=20 , help_text="Enter a Product Color")

    class Meta: 
        verbose_name_plural ="Product Colors"

    def __str__(self):
        return self.name
 
class Product(models.Model):
    slug=models.SlugField(allow_unicode=True)
    name = models.CharField(max_length=150)
    brand = models.ForeignKey(Brand,on_delete=models.SET_NULL,null=True,blank=True)
    color = models.ForeignKey(Color , help_text="Select Color of the product",on_delete=models.SET_NULL,null=True,blank=True)
    
    desc = models.TextField(max_length=255 ,null=True, blank=True)
    mini_desc = models.CharField(max_length=200)
    
    category =  models.ManyToManyField(Category)
    inventory = models.ForeignKey(Inventory,on_delete=models.SET_NULL,null=True)
    price = models.PositiveBigIntegerField(null=True,blank=True)
    discount = models.ForeignKey(Discount,on_delete=models.SET_NULL,null=True,blank=True)
    status = models.BooleanField(default=True)
    
    cover = models.ImageField(
        upload_to= 'static/images/products/{0}'.format(strftime('%Y%m%d-%H%M%S',gmtime())) ,
        default='no-image.jpg' ,
        width_field='imagewidth' ,
        height_field='imageheight' ,
    )
    pic1 = models.ImageField(
        upload_to= 'static/images/products/{0}'.format(strftime("%Y%m%d - %H%M%S",gmtime())) ,
        default = 'no-image.jpg' ,
        null = True, blank = True ,
    )
    pic2 = models.ImageField(
        upload_to= 'static/images/products/{0}'.format(strftime("%Y%m%d - %H%M%S",gmtime())) ,
        default = 'no-image.jpg' ,
        null = True ,blank = True ,
    )
    pic3 = models.ImageField(
        upload_to= 'static/images/products/{0}'.format(strftime("%Y%m%d - %H%M%S",gmtime())) ,
        default = 'no-image.jpg' ,
        null = True, blank = True,
    )
    pic4 = models.ImageField(
        upload_to= 'static/images/products/{0}'.format(strftime("%Y%m%d - %H%M%S" ,gmtime())) ,
        default = 'no-image.jpg' ,
        null = True, blank = True ,
    )
    
    imagewidth = models.PositiveIntegerField(editable = False, default = 401)
    imageheight = models.PositiveIntegerField(editable = False, default = 401)
    
    rate = models.IntegerField(default=0, max_length =3)
    counted_view=  models.IntegerField(default=0)
    tags = TaggableManager()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField()
    
    class Meta:
        verbose_name_plural = "Products"
        ordering = ('-created_at',)
    # Adding brand to admin prepopulated_fields dictionary only returns id ,
    # One way to do is adding save method 
    def save(self):
        if not self.id: # if this is a new item
            newslug = '{0} {1}'.format(self.brand, self.name)  
            self.slug = slugify(newslug)
        super(Product, self).save()

    def __str__(self):
        return self.name
    
    
    
    
    
    

class Contact(models.Model):

    name=models.CharField(max_length=255)
    email=models.EmailField()
    phone = models.CharField(max_length=11,null=True, blank=True)
    subject=models.CharField(max_length=255,blank=True,null=False)
    message=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('create_at',)

"""
class Newsletter (models.Model):

    email = models.EmailField() 
    def __str__(self):
        return self.email    
"""  