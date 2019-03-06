from django.contrib import admin
from meal_deal.models import Category, Meal_Deal

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category, CategoryAdmin)
admin.site.register(Meal_Deal)

# Register your models here.
