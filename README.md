# Martin Kiuna — Portfolio

Personal portfolio for Martin Kiuna, software engineer (AI systems · security · backend).
Built with **Django + Whitenoise**, deployed on **Vercel**.

## Stack

- **Django 5.2 LTS** — templating and routing only; no database required
- **All content lives in [core/data.py](core/data.py)** — projects, case studies,
  skills, timeline, profile links. Edit that file to change the site; nothing else
  needs touching. `core/tests.py` validates the data schema, so a typo fails tests
  instead of silently dropping a page section.
- **No client-side frameworks** — one small vanilla JS file, one CSS design system
  built on custom-property tokens ([static/css/style.css](static/css/style.css))
- **Fonts are self-hosted** in [static/fonts/](static/fonts/) (Inter + JetBrains Mono
  woff2 subsets) — no third-party CDN request, GDPR-friendly

## Local development

```bash
python -m venv venv            # note: the committed venv/ is broken; recreate it
venv\Scripts\activate          # Windows
pip install -r requirements.txt
python manage.py runserver     # http://127.0.0.1:8000
```

Static files are served by the dev server in DEBUG mode; nothing else needed.

## Tests & checks

```bash
python manage.py check
python manage.py test          # 18 tests: routes, filters, 404, SEO, data schema
```

## Adding a project

1. Add a dict to `PROJECTS` in [core/data.py](core/data.py) with all keys used by
   existing entries (`id`, `title`, `short_desc`, `full_desc`, `impact`, `stack`,
   `categories`, `icon`, `github`, `demo`, `featured`, `role`, `problem`,
   `solution`, `features`, `architecture`, `learned`).
2. If it uses a new category slug, add it to `CATEGORIES` (filter tabs render from
   that list; unknown slugs fail tests).
3. Optionally add `static/img/og/<project-id>.png` (1200×630) for a rich social
   share card; the site-wide card is used as fallback.
4. Run `python manage.py test` — the schema validator catches missing keys.

## Deployment (Vercel)

- `vercel.json` ships `staticfiles/` via `@vercel/static` (served at `/static/*`)
  and routes everything else to `portfolio/wsgi.py`, where Whitenoise serves
  static files as a fallback. **Run `python manage.py collectstatic --noinput`
  and commit the output whenever `static/` changes** — the deploy serves what's
  in the repo.
- Security headers (HSTS, HTTPS redirect, secure cookies) activate only when
  Vercel's `VERCEL_ENV` is present, so local dev over http keeps working.
- Pages are cached server-side for 1 hour (`cache_page`) — content is read-only,
  so this is safe. Drop the decorator in [core/views.py](core/views.py) if you
  later add dynamic content.

## Asset notes

- `static/img/profile.jpg` — square, 400×400, ~30KB (sized for the 96px avatar)
- `static/img/martin-kiuna-cv.pdf` — keep under ~300KB; a 4MB CV is a slow
  first impression
- `static/img/og/og-site.png` (1200×630, <300KB) — used for `og:image` everywhere;
  per-project cards override it by convention `og/<project-id>.png`
