from django.shortcuts import render
from django.http import HttpResponse
from meal_deal.models import Category
from meal_deal.models import Meal_Deal
from meal_deal.forms import CategoryForm

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

def register(request):
    registered=False
    if request.method == 'POST':
        user_form=UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture= request.FILES['picture']

            profile.save()

            registered= True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileForm()
    return render(request,
                    'meal_deal/register.html',
                    {'user_form': user_form,
                    'profile_form': profile_form,
                    'registered': registered})
    
