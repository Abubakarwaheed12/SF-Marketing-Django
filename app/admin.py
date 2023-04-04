from django.contrib import admin
from app.models import Services, Contact , Testimonials
# Register your models here.

@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display=['id' ,'name','designation','review' , 'company','companyImage','image']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['id' ,'name','email','message']


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display=['id' ,'name','desc']