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
        {"title": "Scott's Meal Deal", "description": "ham and cheese sandwich, orange tropicana and ready salted crisps", "pic": NEW_DIR + "Scott.jpg"},
        {"title": "Stewart's Meal Deal","description": "chicken bacon and stuffing crisps, salt and vinegar kettle chips and a diet coke", "pic":NEW_DIR+"Stewart.jpg"},
        {"title": "Jacob's Meal Deal","description": "chicken avocado and bacon sandwich, sunbites and some tropical juice", "pic":NEW_DIR+"Jacob.jpg"}
        ]
    other_pages = [
        {"title": "Erce's Meal Deal","description": "Sausage, bacon and egg triple sandwich, apple juice and sweet chilly sensations", "pic":NEW_DIR+"Erce.jpg"},
        {"title": "Luke's Meal Deal","description": "Chicken+bacon pasta, apple juice, salt and vinegar crips", "pic":NEW_DIR+"Luke.jpg"},
        {"title": "Paolo's Meal Deal","description": "tomato chicek and chorizo pasta with a lucosade and a packet of flame grilled steak mccoys", "pic":NEW_DIR+"Paolo.jpg"}
        ]
    meaty_pages = [
        {"title": "Beth's Meal Deal","description": "Sausage bacon and egg sandwich, a galaxy bar and an innocent bubbles lemon and lime juice", "pic":NEW_DIR+"Beth.jpg"},
        {"title": "Joseph's Meal Deal","description": "Fanta orange, flame grilled steak mccoys and a prawn mayo sandwich", "pic":NEW_DIR+"Joseph.jpg"},
        {"title": "Andrew's Meal Deal", "description": "Prawn, mango and chilli wrap, apple+grape bag and a diet coke", "pic":NEW_DIR+"Andrew.jpg"}
        ]

    cats = {"Vegetarian": {"meals": vegetarian_pages, "likes": 0},
            "Meaty": {"meals": meaty_pages, "likes": 1},
            "Others": {"meals": other_pages, "likes": 2} }

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["meals"]:
            add_page(c, p["title"], p["description"], p["pic"])

    for c in Category.objects.all():
        for p in Meal_Deal.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))
            
def add_page(cat, title, description, pic, views=0):
    p = Meal_Deal.objects.get_or_create(category=cat, title=title)[0]
    p.views=views
    p.description=description
    p.pic = pic
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

if __name__ == '__main__':
    print("Starting Meal Deal population script...")
    populate()
