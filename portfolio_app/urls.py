# portfolio_app/urls.py
from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import Sitemap
from .models import Project

class ProjectSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Project.objects.all()

    def lastmod(self, obj):
        return obj.date

sitemaps = {
    'projects': ProjectSitemap,
}

urlpatterns = [
    path('', views.home, name='home'),  # Home page URL
    path('projects/', views.projects, name='projects'),  # Projects page URL
    path('about/', views.about, name='about'),  # About page URL
    path('contact/', views.contact, name='contact'),
    
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),# Contact page URL
]
