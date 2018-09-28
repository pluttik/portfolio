from django.db import models

class Business(models.Model):
    business_name = models.CharField(max_length=200)
    business_mission = models.CharField(max_length=400)
    business_about = models.CharField(max_length=2000)
    business_colour = models.CharField(max_length=200)
    business_photo = models.CharField(max_length=200)
    
class Service(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=200)
    service_text = models.CharField(max_length=200)
    service_icon = models.CharField(max_length=200)