from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
# Create your views here.

# Home View

class HomeView(View):
    
    template_name='index.html'
    
    def get(self , request ,  *args,**kwargs):
        
        context={}
        
        return render(request, self.template_name)


# Services View 

class Services(View):
    
    template_name='services.html'
    
    def get(self , request , *args,**kwargs):
        
        context={}
        
        return render(request, self.template_name)
    
    

# About View 

class About(View):
    
    template_name='about.html'
    
    def get(self , request , *args,**kwargs):
        
        context={}
        
        return render(request, self.template_name)
    
    
# CaseStudies View 

class CaseStudies(View):
    
    template_name='case_studies.html'
    
    def get(self , request , *args,**kwargs):
        
        context={}
        
        return render(request, self.template_name)
    
    
# Workflow 

class Workflow(View):
    
    template_name='workflow.html'
    
    def get(self , request , *args,**kwargs):
        
        context={}
        
        return render(request, self.template_name)