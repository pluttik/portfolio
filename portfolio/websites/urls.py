from django.urls import path

from . import views

app_name = 'websites'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:business_id>/home/', views.home, name='home'),
    path('<int:business_id>/about/', views.about, name='about'),
    path('<int:business_id>/contact/', views.contact, name='contact'),
]