from django.shortcuts import render , redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from app.models import Testimonials as testimonials
from app.models import Services as  services
from app.models import Contact as  contacts
from app.models import BlogPost as blogs
from django.core.mail import send_mail
from django.conf import settings
import threading

# Create your views here.
# Email Thread 

class EmailThread(threading.Thread):

    def __init__(self, request, email, message):
        self.request = request
        self.email = email
        self.message = message
        
        
        threading.Thread.__init__(self)

    def run(self):
        subject = 'Contact'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [self.email]
        message = self.message
        send_mail(subject, message, email_from, recipient_list)


# Home View

class HomeView(View):

    template_name='templates/index.html'
    
    def get(self , request):
        service=services.objects.all()
        reviews=testimonials.objects.all()
        print(reviews)
        context={'services':service , 'reviews' : reviews}
        
        
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
        web_url=request.POST.get('web')
        budget=request.POST.get('budget')
        serv=request.POST.get('serv')
        message=request.POST.get('message')

        allmessage = f'name : {name} \n email : {email} \n  Url : {web_url} \n budget : {budget} \n Service of Interest : {serv} \n Message : {message} '
        

        print(name , email , message , web_url , budget , serv)
        if name and email:
            contacts.objects.create(name=name , email=email ,website_url=web_url, budget=budget, service_of_interest=serv , message=message)
            print('message sent successfully ...!!')
            messages.success(request, 'Thank You..')
            mail = 'saniaa.faroooq@gmail.com'
            EmailThread(request , mail , allmessage).start()
            
            

        return redirect(f'{self.request.path_info}')
    
    

# Blog 
class Blog(View):
    
    template_name='templates/blog.html'
    
    def get(self , request , *args,**kwargs):
        
        posts=blogs.objects.all()
        
        context={'posts':posts}
        
        return render(request, self.template_name , context)
  
  
# Single Post 
class SingleBlog(View):
    
    template_name='templates/single_post.html'
    
    def get(self , request , id,  *args,**kwargs):
        
        post=blogs.objects.get(id=id)
        
        context={'post':post}
        print(post)
        return render(request, self.template_name, context)
  
  
  
    
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
    
    
# 404 Page 
def error_404(request , exception):
    return render(request, 'templates/404.html')
