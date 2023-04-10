from django.db import models

# Create your models here.

class Testimonials(models.Model):
    name=models.CharField(max_length=100)
    designation=models.CharField(max_length=200 , null=True , blank=True)
    review=models.TextField()
    image=models.ImageField(upload_to='media/testimonial_images' ,  null=True , blank=True)

    
    
    def __str__(self):
        return self.name
    

# Contact Form
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    message=models.CharField(max_length=2000)
    
    
    

    def __str__(self):
        return self.name
    

# Services

class Services(models.Model):
    name=models.CharField(max_length=200)
    desc=models.CharField(max_length=2000)


    
    def __str__(self):
        return self.name