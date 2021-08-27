from django.utils.text import slugify
import random 


# create unique auto sluf 
def unique_slug_generator(instance, new_slug = None): 
    if new_slug is not None: 
        slug = new_slug 
    else: 
        slug = slugify(instance.en_title) 
    Klass = instance.__class__ 
    qs_exists = Klass.objects.filter(slug = slug).exists() 
      
    if qs_exists:
        randstr = random.randint(300_000, 500_000)
        new_slug = f"{slug}-{randstr}"
        return unique_slug_generator(instance, new_slug = new_slug) 
    return slug 