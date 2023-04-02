from django.db import models

# Create your models here.

class Testimonials(models.Model):
    name=models.CharField(max_length=100)
    designation=models.CharField(max_length=200)
    review=models.TextField()
    image=models.ImageField(upload_to='media')
    company=models.CharField(max_length=200)
    companyImage=models.ImageField(upload_to='media')

