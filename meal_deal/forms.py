from django import forms
from meal_deal.models import Meal_Deal, Category, UserProfile, Comment
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the category name.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)

class MealDealForm(forms.ModelForm):
    #image = forms.ImageField()
    title = forms.CharField(max_length=128,
                            help_text="Title: ")
    description = forms.CharField(max_length=1000,
                            help_text="Description: ")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Meal_Deal
        fields = ('pic', 'title', 'description', 'category')
        #exclude = ('category',)

# User Authentication 
                                       
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    
    class Meta:
        model = UserProfile
        exclude = ('user', )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)



