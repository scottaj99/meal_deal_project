import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'meal_deal_project.settings')

import django
django.setup()
from meal_deal.models import Category, Meal_Deal
from meal_deal_project.settings import MEDIA_DIR
NEW_DIR = MEDIA_DIR + "/uploads/"
NEW_DIR = NEW_DIR.replace("\\", "/")
def populate():
    vegetarian_pages = [
        {"title": "Scott's Meal Deal", "description": "test", "picture": NEW_DIR + "Scott.jpg"},
        {"title": "Stewart's Meal Deal","description": "test", "picture":"meal_deal_project/media/uploads/Stewart.jpg"},
        {"title": "Jacob's Meal Deal","description": "test", "picture":"meal_deal_project/media/uploads/Jacob.jpg"}
        ]
    other_pages = [
        {"title": "Erce's Meal Deal","description": "test", "picture":"meal_deal_project/media/uploads/Erce.jpg"},
        {"title": "Luke's Meal Deal","description": "test", "picture":"meal_deal_project/media/uploads/Luke.jpg"},
        {"title": "Paolo's Meal Deal","description": "test", "picture":"meal_deal_project/media/uploads/Paolo.jpg"}
        ]
    meaty_pages = [
        {"title": "Beth's Meal Deal","description": "test", "picture":"meal_deal_project/media/uploads/Beth.jpg"},
        {"title": "Joseph's Meal Deal","description": "test", "picture":"meal_deal_project/media/uploads/Joseph.jpg"},
        {"title": "Andrew's Meal Deal", "description": "test", "picture":"meal_deal_project/media/uploads/Andrew.jpg"}
        ]

    cats = {"Vegetarian": {"meals": vegetarian_pages},
            "Meaty": {"meals": meaty_pages},
            "Others": {"meals": other_pages} }

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["meals"]:
            add_page(c, p["title"], p["description"], p["picture"])

    for c in Category.objects.all():
        for p in Meal_Deal.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))
            
def add_page(cat, title, description, picture, views=0):
    p = Meal_Deal.objects.get_or_create(category=cat, title=title)[0]
    p.views=views
    p.description=description
    p.picture = picture
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

if __name__ == '__main__':
    print("Starting Meal Deal population script...")
    populate()
