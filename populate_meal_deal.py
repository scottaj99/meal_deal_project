import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'meal_deal_project.settings')

import django
django.setup()
from meal_deal.models import Category, Meal_Deal

def populate():
    vegetarian_pages = [
        {"title": "Scott's Meal Deal"},
        {"title": "Stewart's Meal Deal"},
        {"title": "Jacob's Meal Deal"}
        ]
    other_pages = [
        {"title": "Erce's Meal Deal"},
        {"title": "Luke's Meal Deal"},
        {"title": "Paolo's Meal Deal"}
        ]
    meaty_pages = [
        {"title": "Beth's Meal Deal"},
        {"title": "Joseph's Meal Deal"},
        {"title": "Andrew's Meal Deal"}
        ]

    cats = {"Vegetarian": {"meals": vegetarian_pages},
            "Meaty": {"meals": meaty_pages},
            "Others": {"meals": other_pages} }

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["meals"]:
            add_page(c, p["title"])

    for c in Category.objects.all():
        for p in Meal_Deal.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))
            
def add_page(cat, title, views=0):
    p = Meal_Deal.objects.get_or_create(category=cat, title=title)[0]
    p.views=views
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

if __name__ == '__main__':
    print("Starting Meal Deal population script...")
    populate()
