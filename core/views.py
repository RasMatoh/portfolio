from django.shortcuts import render
from .data import PROJECTS, SKILLS, STATS


def home(request):
    featured = [p for p in PROJECTS if p.get('featured')]
    return render(request, 'home.html', {'projects': featured})


def projects(request):
    category = request.GET.get('category', 'all')
    if category == 'all':
        filtered = PROJECTS
    else:
        filtered = [p for p in PROJECTS if category in p['categories']]
    return render(request, 'projects.html', {
        'projects': filtered,
        'active_category': category,
    })


def about(request):
    # Convert to list of tuples for safe Django template iteration
    skills_list = [(group, items) for group, items in SKILLS.items()]
    return render(request, 'about.html', {
        'skills_list': skills_list,
        'stats': STATS,
    })


def contact(request):
    return render(request, 'contact.html')