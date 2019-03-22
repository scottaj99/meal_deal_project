from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self): # For Python 2, use __unicode__ too
        return self.name
    
class Meal_Deal(models.Model):

    pic = models.ImageField(upload_to = 'uploads', null=True)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1000)
    price = models.FloatField(null=True, blank=True, default=None)
    slug = models.SlugField(unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    
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
    picture = models.ImageField(upload_to='profile_images', null=True)


    #Override the __unicode__() method to return out something meaningful
    def __str__(self):
        return self.user.username

class Comment(models.Model):
    post = models.ForeignKey(Meal_Deal)
    user = models.ForeignKey(User)
    content = models.TextField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.post.title, str(self.user.username))
