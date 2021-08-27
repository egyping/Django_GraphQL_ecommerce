from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from mptt.models import MPTTModel, TreeForeignKey




class Category(MPTTModel):
    en_title = models.CharField(verbose_name='English title', max_length=200, null=True, blank=True)
    ar_title = models.CharField(verbose_name='Areabic title', default="أسم البراند بالعربي", max_length=200, null=True, blank=True)
    en_description = models.CharField(verbose_name='English Description',default="Category English Description", max_length=200, null=True, blank=True)
    ar_description = models.CharField(verbose_name='Arabic Description',default="وصف الكاتجوري بالعربي", max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=255, blank=True, unique=True)
    cat_image = models.ImageField(upload_to='catalog/categories', blank=True)

    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.en_title

# Slug generator signal
def pre_save_receiver(sender, instance, *args, **kwargs): 
   if not instance.slug: 
       instance.slug = unique_slug_generator(instance) 
pre_save.connect(pre_save_receiver, sender = Category) 



class Brand(models.Model):
    en_title = models.CharField(verbose_name='English title', max_length=200, null=True, blank=True)
    ar_title = models.CharField(verbose_name='Arabic title', default="أسم الكاتجوري بالعربي", max_length=200, null=True, blank=True)
    en_description = models.CharField(verbose_name='English Description',default="Brand Description", max_length=200, null=True, blank=True)
    ar_description = models.CharField(verbose_name='Arabic Description',default="وصف الكاتجوري بالعربي", max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=255, blank=True, unique=True)
    cat_image = models.ImageField(upload_to='catalog/brands', blank=True)

    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'brands'

    def __str__(self):
        return self.en_title

# Slug generator signal
def pre_save_receiver(sender, instance, *args, **kwargs): 
   if not instance.slug: 
       instance.slug = unique_slug_generator(instance) 
pre_save.connect(pre_save_receiver, sender = Brand) 



class Product(models.Model):
    en_title = models.CharField(verbose_name='English title', max_length=200, null=True, blank=True)
    ar_title = models.CharField(verbose_name='Arabic title',default="أسم المنتج بالعربي", max_length=200, null=True, blank=True)
    en_description = models.CharField(verbose_name='English Description', default="Product Description", max_length=200, null=True, blank=True)
    ar_description = models.CharField(verbose_name='Arabic Description', default="وصف المنتج بالعربي", max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=255, blank=True, unique=True)
    thumb_img = models.ImageField(verbose_name='Thumbnail Image', upload_to='catalog/prod_thumbs', blank=True)

    product_status = models.BooleanField(verbose_name='Is Active', default=1, blank=True)
    sku = models.CharField(max_length=50, null=True, blank=True, unique=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True, blank=True)
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE, null=True, blank=True)

    cost_price = models.DecimalField(verbose_name='Cost Price',default=20.00, max_digits=10, decimal_places=2, null=True, blank=True)
    sale_price = models.DecimalField(verbose_name='Retail Price',default=40.00, max_digits=10, decimal_places=2, null=True, blank=True)

    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.en_title

# Slug generator signal
def pre_save_receiver(sender, instance, *args, **kwargs): 
   if not instance.slug: 
       instance.slug = unique_slug_generator(instance) 
pre_save.connect(pre_save_receiver, sender = Product) 


class ProductVariant(models.Model):
    DISPLAY_CHOICES = (
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
        ('xlarge', 'X Large'),
    )
    product = models.ForeignKey(Product, related_name='product_variants', on_delete=models.CASCADE, null=True, blank=True)
    size = models.CharField(verbose_name='Size',max_length=50, choices=DISPLAY_CHOICES, null=True, blank=True)
    stock = models.IntegerField(verbose_name='Stock', default=10, null=True, blank=True)
    child_sku = models.CharField(verbose_name='SKU', max_length=50, null=True, blank=True, unique=True)

    class Meta:
        db_table = "product_variants"

    def __str__(self):
        return self.size


class ProductImages(models.Model):
    product = models.ForeignKey(Product, related_name='product_images', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Image', upload_to='catalog/prod_images', blank=True)

    class Meta:
        db_table = "product_images"

    
    def __str__(self):
        template = '{0.product} {0.image}'
        return template.format(self)
