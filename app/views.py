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

