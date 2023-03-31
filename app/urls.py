from django.urls import path , include
from app.views import HomeView


urlpatterns=[
    path('' , HomeView.as_view()),
]