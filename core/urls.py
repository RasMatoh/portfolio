from django.urls import path
from . import views

urlpatterns = [
    path('',                   views.home,           name='home'),
    path('projects/',          views.projects,       name='projects'),
    path('projects/<slug:project_id>/', views.project_detail, name='project_detail'),
    path('about/',             views.about,          name='about'),
    path('contact/',           views.contact,        name='contact'),
    path('robots.txt',         views.robots,         name='robots'),
    path('sitemap.xml',        views.sitemap,        name='sitemap'),
]
