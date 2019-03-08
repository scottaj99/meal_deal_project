from django.db import models
from django.template.defaultfilters import slugify

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
    #url = models.URLField()
    views = models.IntegerField(default=0)
    def __str__(self): # For Python 2, use __unicode__ too
        return self.title

# Create your models here.