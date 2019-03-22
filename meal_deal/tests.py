from django.test import TestCase
from meal_deal.models import Category, Meal_Deal, UserProfile, Comment
from django.core.urlresolvers import reverse
from django.conf import settings
import os
import population_script

# Create your tests here.



class mealDealTesting(TestCase):
    # Test catagory can be created
    def create_category(self, name="Quick test catagory hi"):
        return Category.objects.create(name=name)

    def test_category_creation(self):
        print("---------------------Catagory Test------------------------------")
        print("Testing creation of category...")
        cat = self.create_category()
        self.assertTrue(isinstance(cat, Category))
        self.assertEqual(cat.name, "Quick test catagory hi")
        print("")


                        
    # Test base template exists
    def test_base_exists(self):
        print("---------------------Template test-------------------------------")
        print("Testing presence of base template...")
        path_to_base = settings.TEMPLATE_DIR + '/meal_deal/base.html'
        self.assertTrue(os.path.isfile(path_to_base))
        print("")


    # Test population scrit
    
    def test_population_script_changes(self):
        print("---------------------Testing population script-------------------------------")
        #Populate database
        population_script.populate()

        # Check if the one meal deal has correct number of likes and dislikes
        meal = Meal_Deal.objects.get(title="Scott's Meal Deal")
        self.assertEquals(meal.likes, 9)
        self.assertEquals(meal.dislikes, 6)

         # Check if the one meal deal has correct number of likes and dislikes
        meal = Meal_Deal.objects.get(title="Luke's Meal Deal")
        self.assertEquals(meal.likes, 2)
        self.assertEquals(meal.dislikes, 261)

        # Check if the one meal deal has correct number of likes and dislikes
        meal = Meal_Deal.objects.get(title="Andrew's Meal Deal")
        self.assertEquals(meal.likes, 3)
        self.assertEquals(meal.dislikes, 5)
            
        
