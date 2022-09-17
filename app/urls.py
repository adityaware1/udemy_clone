from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index,name='home'),
    path('development', views.development,name='development'),
    path('business', views.business,name='business'),
    path('marketing', views.marketing,name='marketing'),
    path('ai', views.ai,name='ai'),
    path('ml', views.ml,name='ml'),
    path('contact', views.contact,name='contact')
    
]