from django.urls import path , include
from app.views import HomeView , Services , Workflow , CaseStudies , About , Contact , Blog
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('' , HomeView.as_view() , name='home'),
    path('Services' , Services.as_view() , name='services'),
    path('Workflow' , Workflow.as_view() , name='workflow'),
    path('Blog' , CaseStudies.as_view() , name='Blog'),
    path('About' , About.as_view() , name='about'),
    path('contact', Contact.as_view() , name='contact')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)