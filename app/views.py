from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from app.models import Testimonials ,Services , Contact
# Create your views here.

# Home View

class HomeView(View):

    template_name='templates/index.html'
    
    def get(self , request ,  *args,**kwargs):
                
        context={}
        
        return render(request, self.template_name)
    



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
        # if name and email:
        #     Contact.objects.create(name=name , email=email , message=message)
            
            

        return render(request, 'templates/index.html')
    
    

# Blog 
class Blog(View):
    
    template_name='templates/blog.html'
    
    def get(self , request , *args,**kwargs):
        
        context={}
        
        return render(request, self.template_name)
  