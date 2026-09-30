from django.shortcuts import render, Http404
from django.views.decorators.cache import cache_page
from .data import PROJECTS, SKILLS, PROFILE, CATEGORIES, TIMELINE, LEARNING, get_project, related_projects


def home(request):
    featured = [p for p in PROJECTS if p.get('featured')]
    return render(request, 'home.html', {
        'projects': featured,
    })


@cache_page(60 * 60)
def projects(request):
    category = request.GET.get('category', 'all')

    if category == 'all':
        filtered = PROJECTS
    else:
        filtered = [p for p in PROJECTS if category in p['categories']]

    return render(request, 'projects.html', {
        'projects': filtered,
        'active_category': category,
        'categories': CATEGORIES,
    })


@cache_page(60 * 60)
def project_detail(request, project_id):
    project = get_project(project_id)
    if project is None:
        raise Http404(f'No project found with id "{project_id}"')

    return render(request, 'project_detail.html', {
        'project': project,
        'related': related_projects(project),
    })


@cache_page(60 * 60)
def about(request):
    skills_list = list(SKILLS.items())
    return render(request, 'about.html', {
        'skills_list': skills_list,
        'timeline': TIMELINE,
        'learning': LEARNING,
    })


@cache_page(60 * 60)
def contact(request):
    return render(request, 'contact.html')


def robots(request):
    return render(request, 'robots.txt', content_type='text/plain')


def sitemap(request):
    """Hand-rolled sitemap: cheap, exact, no contrib dependency."""
    site = 'https://martinkiruna.vercel.app'
    urls = [
        {'loc': f'{site}/',          'priority': '1.0', 'changefreq': 'monthly'},
        {'loc': f'{site}/projects/', 'priority': '0.9', 'changefreq': 'monthly'},
        {'loc': f'{site}/about/',    'priority': '0.6', 'changefreq': 'yearly'},
        {'loc': f'{site}/contact/',  'priority': '0.6', 'changefreq': 'yearly'},
    ]
    for p in PROJECTS:
        urls.append({'loc': f"{site}/projects/{p['id']}/", 'priority': '0.8', 'changefreq': 'monthly'})
    return render(request, 'sitemap.xml', {'urls': urls}, content_type='application/xml')
