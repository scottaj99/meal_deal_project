from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self): # For Python 2, use __unicode__ too
        return self.name
    
class Meal_Deal(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    #url = models.URLField()
    views = models.IntegerField(default=0)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Meal_Deal, self).save(*args, **kwargs)
    def __str__(self): # For Python 2, use __unicode__ too
        return self.title

# User profiles additional information

class UserProfile(models.Model):
    # Required line to link UserProfile to a User model instance
    user = models.OneToOneField(User)

    # Additional attributes (can add extras)
    picture = models.ImageField(upload_to='profile_images', blank=True)


    #Override the __unicode__() method to return out something meaningful
    def __str__(self):
        return self.user.username
