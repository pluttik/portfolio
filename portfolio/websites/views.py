from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Business

def index(request):
    businesses = Business.objects.all()
    return render(request, 'websites/index.html', {'businesses': businesses})
    
def home(request, business_id):
    try:
        business = Business.objects.get(pk = business_id)
    except Business.DoesNotExist:
        raise Http404("Business does not exist")
    return render(request, 'websites/home.html', {'business': business})
    
def about(request, business_id):
    response = "This will be the about page of the shop with number %s"
    return HttpResponse(response % business_id)
    
def contact(request, business_id):
    response = "This will be the contact page of the shop with number %s"
    return HttpResponse(response % business_id)