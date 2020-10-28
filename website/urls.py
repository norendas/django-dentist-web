from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog-single/', views.blogsingle, name='blogsingle'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('department/', views.department, name='department'),
    path('doctor/', views.doctor, name='doctor'),
    path('main/', views.main, name='main'),
    path('pricing/', views.pricing, name='pricing'),
] 
