from django.shortcuts import render
from django.http import HttpResponse
from meal_deal.models import Category
from meal_deal.models import Meal_Deal
from meal_deal.models import UserProfile
from meal_deal.forms import CategoryForm
from meal_deal.forms import MealDealForm
from meal_deal.forms import UserForm, UserProfileForm
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from datetime import datetime



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
        meal_deal = Meal_Deal.objects.get(slug=meal_deal_slug)
        context_dict['meal_deal'] = meal_deal
    except Category.DoesNotExist:
        context_dict['meal_deal'] = None

    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
        
    response = render(request, 'meal_deal/deals.html', context_dict)
    return response

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

@login_required
def list_profiles(request):
    userprofile_list = UserProfile.objects.all()

    return render(request, 'meal_deal/list_profiles.html',
                  {'userprofile_list' : userprofile_list})
        

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

def add_deal(request):
   # try:
    #    category = Category.objects.get(slug=category_name_slug)
    #except Category.DoesNotExist:
     #   category = None
    form = MealDealForm()

    if request.method == 'POST':
        form = MealDealForm(request.POST, request.FILES)
        if form.is_valid():
            #if category:
            page = form.save(commit=False)

                ## IVE TRIED TO SAVE THE PICTURE SEPERATE HERE, BUT I CANT FIND AN IDENTIFIER
                ## TO PUT IN THE BRACKETS IN THE LINE BELOW
                
                #pic = Meal_Deal.objects.get(name=name)
               # pic.model_pic = form.cleaned_data['image']
               # pic.save()
               # page.category=category
            page.views = 0
            page.save()
            return index(request)
        else:
            print(form.errors)
    context_dict = {'form':form}
    return render(request, 'meal_deal/add_deal.html', context_dict)

@login_required
def like_deal(request):
    dea_id = None
    if request.method == 'GET':
        dea_id = request.GET['deals_id']
    likes=0
    if dea_id:
        dea = Meal_Deal.objects.get(id=int(dea_id))
        if dea:
            likes = dea.likes + 1
            dea.likes = likes
            dea.save()
    return HttpResponse(likes)

@login_required
def dislike_deal(request):
    dea_id = None
    if request.method == 'GET':
        dea_id = request.GET['deals_id']
    dislikes=0
    if dea_id:
        dea = Meal_Deal.objects.get(id=int(dea_id))
        if dea:
            dislikes = dea.dislikes + 1
            dea.dislikes = dislikes
            dea.save()
    return HttpResponse(dislikes)

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(request.COOKIES.get('visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie

    request.session['visits'] = visits









    
