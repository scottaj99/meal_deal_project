from django.contrib import admin
from meal_deal.models import Category, Meal_Deal, Comment
from meal_deal.models import UserProfile

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
class MealDealAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display=('title', 'category', 'description')
admin.site.register(Category, CategoryAdmin)
admin.site.register(Meal_Deal, MealDealAdmin)
admin.site.register(Comment)


