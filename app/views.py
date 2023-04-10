from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from app.models import Testimonials as testimonials
from app.models import Services as  services
from app.models import Contact as  contacts
# Create your views here.

# Home View

class HomeView(View):

    template_name='templates/index.html'
    
    def get(self , request):
        service=services.objects.all()
        print(service)
        context={'services':service}
        
        return render(request, self.template_name, context)
    
    
# def HomeView(request):
#     template_name='templates/index.html'
#     service=ser.objects.all()
#     print(service)
#     context={}
    
#     return render(request, template_name)
    



# Services View 

class Services(View):
    
    template_name='templates/services.html'
    
    def get(self , request , *args,**kwargs):
        
        context={}
        
        return render(request, self.template_name)
    
    

# About View 

class About(View):
    
    template_name='templates/about.html'
    
    def get(self , request , *args,**kwargs):
        
        context={}
        
        return render(request, self.template_name)
    
    
# CaseStudies View 

class CaseStudies(View):
    
    template_name='templates/case_studies.html'
    
    def get(self , request , *args,**kwargs):
        
        context={}
        
        return render(request, self.template_name)
    
    
# Workflow 

class Workflow(View):
    
    template_name='templates/workflow.html'
    
    def get(self , request , *args,**kwargs):
        
        context={}
        
        return render(request, self.template_name)
    

# Contact Form Save View 
class Contact(TemplateView  , ListView):
    model='Contact'
    def get(self, request):
        
        return render(request, 'templates/index.html')
    
    
    def post(self, request , *args , **kwargs):
        
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        
        print(name , email , message)
        if name and email:
            contacts.objects.create(name=name , email=email , message=message)
            print('message sent successfully ...!!')
            messages.success(request, 'Form Submitted Successfully...')
            
            

        return render(request, 'templates/index.html')
    
    

# Blog 
class Blog(View):
    
    template_name='templates/blog.html'
    
    def get(self , request , *args,**kwargs):
        
        context={}
        
        return render(request, self.template_name)
  
  
# Single Post 
class SingleBlog(View):
    
    template_name='templates/single_post.html'
    
    def get(self , request , id,  *args,**kwargs):
        
        print(id)
        
        context={}
        
        return render(request, self.template_name)
  
  
  
    
# Privacy Policy Page 
class Privacy(View):
    
    template_name='templates/privacy.html'
    
    def get(self , request ,  *args,**kwargs):
        
        
        context={}
        
        return render(request, self.template_name)
    

# Terms And Conditions  Page 
class Term_and_Conditions(View):
    
    template_name='templates/terms.html'
    
    def get(self , request ,  *args,**kwargs):
        
        
        context={}
        
        return render(request, self.template_name)