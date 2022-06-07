

from django.urls import path
from pages import views

urlpatterns = [
    path('contact/', views.contact_page, name='contact'),
    path('about/', views.about_page, name='about'),
    path('news/', views.news_page, name='news'),
]