from django.db import models

# Create your models here.

class history(models.Model):
    place=models.CharField(max_length=200)
    designation=models.CharField(max_length=200)
    timeperiod=models.CharField(max_length=100)
    work_done=models.TextField(null=True, blank=True)
    score=models.CharField(max_length=50, null=True, blank=True)
    skill_set=models.TextField(null=True, blank=True)
    image_path = models.CharField(max_length=200, null=True, blank=True)

class skills(models.Model):
    name=models.CharField(max_length=200)
    level=models.CharField(max_length=50)
    image_path = models.CharField(max_length=200, null=True, blank=True)
    
class feedback(models.Model):
    person_name=models.CharField(max_length=200)
    person_email=models.CharField(max_length=200)
    person_contact=models.CharField(max_length=200)
    person_feedback=models.TextField(null=True, blank=True)