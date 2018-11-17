from django.shortcuts import render
from .models import Wine

# Create your views here.
def home(request):
    context={}
    return render(request, 'home.html', context)

def grapes(request):
    context={}
    return render(request, 'grapes.html', context)

def about(request):
    context={}
    return render(request, 'about.html', context)

def contact(request):
    context={}
    return render(request, 'contact.html', context)

def index(request):
    fW = Wine.objects.get(id=1)
    country = fW.country
    description = fW.description
    winery = fW.winery
    return render(request, 'index.html', context = {'country': country, 'description': description, 'winery': winery},)
