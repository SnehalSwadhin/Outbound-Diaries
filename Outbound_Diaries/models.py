from django.db import models

# Create your models here.


class Diary(models.Model):

    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    image = models.ImageField()
    out_university = models.CharField(max_length=100)
    out_place = models.CharField(max_length=20)
    research = models.CharField(max_length=100)
    duration = models.CharField(max_length=20)
    discussion = models.TextField()
