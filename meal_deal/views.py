from django.shortcuts import render
from django.http import HttpResponse
from meal_deal.models import Category
from meal_deal.models import Meal_Deal
from meal_deal.models import UserProfile
from meal_deal.forms import CategoryForm
from meal_deal.forms import MealDealForm
from meal_deal.forms import UserForm, UserProfileForm


#Imports for logging in/out
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    meal_deal_list = Meal_Deal.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'meal_deals':meal_deal_list}
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
        context_dict['meal_deals'] = None
    return render(request, 'meal_deal/category.html', context_dict)

def show_meal_deal(request, meal_deal_slug):
    context_dict = {}
    try:
        #category = Category.objects.get(slug=category_name_slug)
        meal_deal = Meal_Deal.objects.get(slug=meal_deal_slug)
        context_dict['meal_deal'] = meal_deal
        #context_dict['category'] = category
    except Category.DoesNotExist:
        #context_dict['category'] = None
        context_dict['meal_deal'] = None
    return render(request, 'meal_deal/deals.html', context_dict)

@login_required
def register_profile(request):
    form = UserProfileForm()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            
            return redirect('index')
        else:
            print(form.errors)

    context_dict = {'form':form}

    return render(request, 'meal_deal/profile_registration.html', context_dict)

# Each profile
@login_required
def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('index')

    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    form = UserProfileForm(
        {'picture': userprofile.picture})

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
    if form.is_valid():
        form.save(commit=True)
        return redirect('profile', user.username)
    else:
        print(form.errors)
    return render(request, 'meal_deal/profile.html',
        {'userprofile': userprofile, 'selecteduser': user, 'form': form})



def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print (form.errors)
    return render(request, 'meal_deal/add_category.html', {'form': form})

def add_deal(request, category_name_slug):

    try:

        category = Category.objects.get(slug=category_name_slug)

    except Category.DoesNotExist:

        category = None



    form = MealDealForm()

    if request.method == 'POST':

        form = MealDealForm(request.POST)

        if form.is_valid():

            if category:

                deal = form.save(commit=False)

                deal.category = category
                #deal.description = description

                deal.views = 0
                if 'picture' in request.FILES:
                    deal.picture=request.FILES['picture']

                deal.save()

                # probably better to use a redirect here.

            return show_category(request, category_name_slug)

        else:

            print(form.errors)



    context_dict = {'form':form, 'category': category}



    return render(request, 'meal_deal/add_deal.html', context_dict)


