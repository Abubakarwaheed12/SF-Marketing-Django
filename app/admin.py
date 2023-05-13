from django.contrib import admin
from app.models import Services, Contact , Testimonials , BlogPost
# Register your models here.

@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display=['id' ,'name','designation','review' , 'image']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['id' ,'name','email','website_url', 'budget' , 'service_of_interest' ,'message']


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display=['id' ,'name','desc']
    
    

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display=['title' , 'img', 'content_area' , 'created_at' , 'updated_at']