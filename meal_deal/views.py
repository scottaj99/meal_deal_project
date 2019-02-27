from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    context_dict = {'boldmessage': "WAD2 Group Project"}
    return render(request, 'meal_deal/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': "This is the about page!"}
    return render(request, 'meal_deal/about.html', context=context_dict)
