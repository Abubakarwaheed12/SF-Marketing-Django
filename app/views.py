from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView
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
class Contact(View):
    
    def get(self, request , *args , **kwargs):
        
        return render(request, 'templates/index.html')
    
    
    def post(self, request , *args , **kwargs):
        return render(request, 'templates/index.html')