from django.contrib import admin
from meal_deal.models import Category, Meal_Deal
from meal_deal.models import UserProfile

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
class MealDealAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
admin.site.register(Category, CategoryAdmin)
admin.site.register(Meal_Deal, MealDealAdmin)



# Register your models here.
