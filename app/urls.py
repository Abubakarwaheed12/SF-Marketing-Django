from django.urls import path , include
from app.views import HomeView , Services , Workflow , CaseStudies , About , Contact , Blog ,SingleBlog ,Privacy ,Term_and_Conditions
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('' , HomeView.as_view() , name='home'),
    path('Services/' , Services.as_view() , name='services'),
    path('Workflow/' , Workflow.as_view() , name='workflow'),
    path('Blog/' , Blog.as_view() , name='Blog'),
    path('About/' , About.as_view() , name='about'),
    path('contact/', Contact.as_view() , name='contact'),
    path('post<int:id>/', SingleBlog.as_view() , name='post'),
    path('privacy-Policy/' , Privacy.as_view(), name='privacy'),
    path('terms-and-conditions/', Term_and_Conditions.as_view(), name='terms'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)