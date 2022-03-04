from django.db import models

# Create your models here.

class Internship(models.Model):
    # image
    image = models.ImageField(upload_to='images/')
    # name of the internship
    internship_name = models.CharField(max_length=30)
    # name of the employer
    employer_name = models.CharField(max_length=30)
    # link to internship application page
    link = models.URLField(max_length=200)
    # description
    description = models.CharField(max_length=200)