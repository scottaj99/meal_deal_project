from django.shortcuts import render
from django.http import HttpResponse
from meal_deal.models import Category
from meal_deal.models import Meal_Deal
def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'meal_deal/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': "This is the about page!"}
    return render(request, 'meal_deal/about.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        meal_deals = Meal_Deal.objects.filter(category=category)
        context_dict['meal_deals'] = meal_deals
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'meal_deal/category.html', context_dict)
