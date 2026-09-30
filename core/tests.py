from django.test import TestCase
from django.urls import reverse, NoReverseMatch

from .data import PROJECTS, PROFILE, CATEGORIES, TIMELINE, LEARNING, get_project, related_projects


# ── Data layer integrity ─────────────────────────────────────
class DataSchemaTests(TestCase):
    """Guard core/data.py against typos that would silently drop UI sections."""

    def test_project_required_keys(self):
        required = {'id', 'title', 'short_desc', 'full_desc', 'impact', 'stack',
                    'categories', 'icon', 'github', 'featured',
                    'role', 'problem', 'solution', 'features', 'architecture', 'learned'}
        for p in PROJECTS:
            missing = required - set(p)
            self.assertEqual(missing, set(), f"{p.get('id', '?')} missing keys: {missing}")

    def test_project_ids_unique_and_sluggable(self):
        ids = [p['id'] for p in PROJECTS]
        self.assertEqual(len(ids), len(set(ids)))
        for pid in ids:
            self.assertRegex(pid, r'^[a-z0-9]+(-[a-z0-9]+)*$')

    def test_categories_reference_known_slugs(self):
        known = {c['slug'] for c in CATEGORIES} - {'all'}
        for p in PROJECTS:
            unknown = set(p['categories']) - known
            self.assertEqual(unknown, set(), f"{p['id']} has unknown categories: {unknown}")

    def test_image_paths_exist_on_disk(self):
        from django.conf import settings
        for p in PROJECTS:
            if p.get('image'):
                path = settings.BASE_DIR / 'static' / p['image']
                self.assertTrue(path.exists(), f"{p['id']}: missing image file {path}")

    def test_urls_are_well_formed(self):
        for p in PROJECTS:
            self.assertTrue(p['github'].startswith('https://'),
                            f"{p['id']} github must be an absolute https URL")
            if p.get('demo'):
                self.assertTrue(p['demo'].startswith('https://'),
                                f"{p['id']} demo must be an absolute https URL")
        for key in ('github', 'linkedin'):
            self.assertTrue(PROFILE[key].startswith('https://'), f"PROFILE.{key} must be https")
        self.assertIn('@', PROFILE['email'])

    def test_profile_and_collections_shaped(self):
        self.assertTrue(PROFILE['name'] and PROFILE['tagline'] and PROFILE['location'])
        self.assertTrue(all({'period', 'title', 'org', 'desc'} <= set(t) for t in TIMELINE))
        self.assertTrue(all(isinstance(t, str) for t in LEARNING))


# ── Pages ────────────────────────────────────────────────────
class PageTests(TestCase):
    """Every route renders 200 with the right template and key content."""

    def test_home(self):
        r = self.client.get(reverse('home'))
        self.assertEqual(r.status_code, 200)
        self.assertTemplateUsed(r, 'home.html')
        self.assertContains(r, 'Martin Kiuna')
        self.assertContains(r, 'og:image')

    def test_projects_all(self):
        r = self.client.get(reverse('projects'))
        self.assertEqual(r.status_code, 200)
        self.assertTemplateUsed(r, 'projects.html')
        self.assertContains(r, 'AI-Powered Smart Trading Assistant')

    def test_project_filtering_by_category(self):
        r = self.client.get(reverse('projects'), {'category': 'security'})
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Cybersecurity Threat Detection Agent')
        self.assertNotContains(r, 'Movie Ticket Booking System')

    def test_project_filter_empty_category(self):
        r = self.client.get(reverse('projects'), {'category': 'mobile'})
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'No projects in this category yet.')

    def test_about(self):
        r = self.client.get(reverse('about'))
        self.assertEqual(r.status_code, 200)
        self.assertTemplateUsed(r, 'about.html')

    def test_contact(self):
        r = self.client.get(reverse('contact'))
        self.assertEqual(r.status_code, 200)
        self.assertTemplateUsed(r, 'contact.html')
        self.assertContains(r, 'kiunamartin2004@gmail.com')

    def test_every_project_detail_renders(self):
        for p in PROJECTS:
            r = self.client.get(reverse('project_detail', args=[p['id']]))
            self.assertEqual(r.status_code, 200, p['id'])
            self.assertTemplateUsed(r, 'project_detail.html')
            self.assertContains(r, p['title'])
            self.assertContains(r, 'The problem')
            self.assertContains(r, 'Key features')

    def test_unknown_project_404s(self):
        with self.assertRaises(NoReverseMatch):
            reverse('project_detail', args=['../etc/passwd'])
        r = self.client.get('/projects/does-not-exist/')
        self.assertEqual(r.status_code, 404)

    def test_data_helpers(self):
        p = get_project('trading-assistant')
        self.assertIsNotNone(p)
        self.assertIsNone(get_project('nope'))
        related = related_projects(p)
        self.assertTrue(all(q['id'] != p['id'] for q in related))
        self.assertLessEqual(len(related), 2)


# ── SEO plumbing ─────────────────────────────────────────────
class SeoTests(TestCase):
    def test_sitemap_lists_every_route(self):
        r = self.client.get('/sitemap.xml')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r['Content-Type'], 'application/xml')
        body = r.content.decode()
        self.assertIn('https://martinkiruna.vercel.app/', body)
        for p in PROJECTS:
            self.assertIn(f'/projects/{p["id"]}/', body)

    def test_robots_points_to_sitemap(self):
        r = self.client.get('/robots.txt')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r['Content-Type'], 'text/plain')
        self.assertIn('Sitemap:', r.content.decode())

    def test_404_uses_branded_template(self):
        r = self.client.get('/no-such-page/')
        self.assertEqual(r.status_code, 404)
        self.assertTemplateUsed(r, '404.html')
        self.assertContains(r, '404', status_code=404)

    def test_home_has_social_meta(self):
        body = self.client.get(reverse('home')).content.decode()
        self.assertIn('property="og:title"', body)
        self.assertIn('property="og:image"', body)
        self.assertIn('name="twitter:card"', body)
