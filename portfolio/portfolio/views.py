from django.views.generic.base import View
from django.shortcuts import render

from websites.models import Business

class HomePageView(View):
    def get(self, request):
        businesses = {'businesses': Business.objects.all()}
        return render(request, 'websites/index.html', context = businesses)