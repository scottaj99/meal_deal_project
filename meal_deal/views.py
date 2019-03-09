from django.shortcuts import render
from django.http import HttpResponse
from meal_deal.models import Category
from meal_deal.models import Meal_Deal
from meal_deal.forms import CategoryForm
from meal_deal.forms import UserForm, UserProfileForm



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

# REGISTER FOR USER AUTH 
def register(request):
    # Boolean value for telling the template whether the registration was successful
    # Set to false initially. Code changes value to true when registration succeeds.

        registered = False

        # If its an HTTP POST, we're interestedin processing form data

        if request.method == 'POST':
            # Attempt to grab information from the raw form information.
            # Note that we make use of both UserForm and UserProfileForm.
            user_form = UserForm(data=request.POST)
            profile_form = UserProfileForm(data=request.POST)

            # If the two forms are valid...
            if user_form.is_valid() and profile_form.is_valid():
                # Save the user's form data to the database.
                user = user_form.save()

                # Now we hash the password with the set_password method
                # Once hashed, we can update the user object

                user.set_password(user.password)
                user.save()

                # Sort out the UserProfile instance
                # Set commit to false to delay saving model until ready

                profile = profile_form.save(commit=False)
                profile.user = user

                # Did user provide a profile picture? Get it from input form and put in
                # UserProfile model

                if 'picture' in request.FILES:
                    profile.picture = request.FILES['picture']


                # Now save the UserProfile model instance
                profile.save()

                # Update our variable to indicate templeate registration success
                registered = True

            else:
                # Invalid form or forms, print problems
                print(user_form.errors, profile_form.errors)

        else:
            # Not a HTTP POST, so render form using two ModelForm instances
            # These forms blank, ready for user input
            user_form = UserForm()
            profile_form = UserProfileForm()


        # Render template depending on context
        return render(request,
                    'meal_deal/register.html',
                    {'user_form': user_form,
                     'profile_form': profile_form,
                     'registered': registered})
