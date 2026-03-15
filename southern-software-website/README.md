# Southern Software, Inc. — Website Redesign

A modern redesign of [southernsoftware.com](https://www.southernsoftware.com), inspired by the dark, professional aesthetic of [nucleuspsp.com/Nucleus](https://nucleuspsp.com/Nucleus/).

## Design Direction

- **Dark public safety aesthetic** — deep navy backgrounds, glowing blue accents, subtle grid overlays
- **Typography** — Barlow Condensed (headings, condensed + bold) + Inter (body)
- **Animations** — fade-up on scroll using IntersectionObserver, no dependencies
- **Fully responsive** — mobile-first, collapses gracefully at 960px and 600px breakpoints
- **No frameworks or build tools required** — plain HTML, CSS, and vanilla JS

## Project Structure

```
southern-software-website/
├── index.html                  ← Main homepage
├── README.md
├── assets/
│   ├── css/
│   │   └── styles.css          ← Full design system (CSS variables, components, layout)
│   ├── js/
│   │   └── main.js             ← Scroll animations, nav behavior, form handling
│   └── img/
│       └── (place logo and image assets here)
└── pages/
    ├── ps-overview.html        ← Public Safety product page (to be built)
    ├── fms-overview.html       ← Financial Management product page (to be built)
    ├── mission.html
    ├── testimonials.html
    ├── involvement.html
    ├── faith.html
    ├── prayer-list.html
    ├── downloads.html
    ├── regionaltrainings.html
    ├── QMStraining.html
    ├── executive-staff.html
    ├── administrative-staff.html
    ├── management-staff.html
    ├── sales-staff.html
    ├── ps-training-staff.html
    ├── ps-support-staff.html
    ├── fms-staff.html
    ├── ps-updates-staff.html
    ├── install-staff.html
    ├── project-management-staff.html
    ├── ps-support-triage.html
    ├── termsofservice.html
    └── privacy.html
```

## Sections (index.html)

| Section | ID | Description |
|---|---|---|
| Top Bar | — | Utility links: phone, support emails, remote support, portal |
| Navigation | — | Sticky, blur-on-scroll, full dropdown menus, mobile toggle |
| Hero | `#top` | Headline, CTAs, stats, feature cards |
| Who We Are | `#about` | Company history, facts grid, tags |
| Products | `#products` | PS Suite card, FMS Suite card, Nucleus callout |
| Support | `#support` | 6 support cards linking to teams and resources |
| Training | `#training` | 2026 regional schedule + virtual classes |
| Partners | — | 10 strategic partners |
| Contact | `#contact` | Info + contact form |
| Footer | — | Brand, links, copyright |

## Getting Started

### Local Development

No build step required. Just open `index.html` in a browser:

```bash
# Option 1 — Direct file open
open index.html

# Option 2 — Local server (recommended to avoid font CORS issues)
npx serve .
# or
python3 -m http.server 8080
```

### GitHub Pages Deployment

1. Push this repository to GitHub
2. Go to **Settings → Pages**
3. Set source to **Deploy from a branch** → `main` → `/ (root)`
4. Your site will be live at `https://yourusername.github.io/southern-software-website/`

### Custom Domain

1. Add a `CNAME` file to the repo root containing your domain:
   ```
   www.southernsoftware.com
   ```
2. Update your DNS:
   - Add a `CNAME` record pointing to `yourusername.github.io`
   - Or use `A` records pointing to GitHub Pages IPs (see [GitHub docs](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site))

## Adding Logo Images

Replace the `SS` text mark in the nav and footer with your actual logo:

1. Place your logo files in `assets/img/`:
   - `logo-white.png` — white version for nav/footer
   - `logo-dark.png` — dark version (if needed)

2. In `index.html`, replace `.nav-logo-mark` blocks with:
   ```html
   <img src="assets/img/logo-white.png" alt="Southern Software" height="36" />
   ```

## Building Inner Pages

Each inner page should include the same `<head>`, nav, and footer from `index.html`. A shared template pattern:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Page Title — Southern Software</title>
  <link rel="stylesheet" href="../assets/css/styles.css" />
</head>
<body>
  <!-- copy topbar + nav from index.html -->
  
  <main>
    <!-- page content here -->
  </main>

  <!-- copy footer from index.html -->
  <script src="../assets/js/main.js"></script>
</body>
</html>
```

Note the `../` path prefix for pages in the `/pages/` subdirectory.

## CSS Architecture

All styles live in `assets/css/styles.css`, organized as:

1. **CSS Variables** — colors, fonts, radii, shadows
2. **Reset** — minimal, box-sizing, smooth scroll
3. **Utility classes** — `.container`, `.section`, `.eyebrow`, `.section-title`, `.fade-up`
4. **Buttons** — `.btn`, `.btn-primary`, `.btn-outline`, `.btn-teal`, `.btn-lg`
5. **Component blocks** — topbar, nav, hero, who-we-are, products, support, training, partners, contact, footer
6. **Responsive breakpoints** — 960px (tablet), 600px (mobile)

## Color Palette

| Variable | Value | Usage |
|---|---|---|
| `--c-bg` | `#06101f` | Page background |
| `--c-bg-2` | `#0b1a2e` | Alternate section bg |
| `--c-bg-3` | `#0f2240` | Card hover states |
| `--c-blue` | `#1b6fe8` | Primary action color |
| `--c-blue-light` | `#4a90f5` | Highlights, links |
| `--c-teal` | `#00c4a0` | FMS accent, eyebrows |
| `--c-text` | `#ccd9ee` | Body text |
| `--c-muted` | `#6b89aa` | Secondary text |
| `--c-dim` | `#3d5470` | Labels, placeholders |

## Contact Form

The form in `index.html` is a front-end-only demo. To make it functional, connect it to a backend. Options:

- **Formspree** (no backend needed): Add `action="https://formspree.io/f/YOUR_ID"` and `method="POST"` to the `<form>` tag, then remove the JS submit handler from `main.js`
- **Netlify Forms**: Add `netlify` attribute to `<form>` if deploying on Netlify
- **EmailJS**: Call their API from the JS submit handler
- **Custom backend**: POST to your PHP/Node endpoint

## Browser Support

Targets modern browsers (Chrome, Firefox, Safari, Edge). Uses:
- CSS custom properties (variables)
- CSS Grid and Flexbox
- IntersectionObserver API
- `backdrop-filter` (graceful fallback in older browsers)

---

*Built for Southern Software, Inc. — Southern Pines, NC — Est. 1988*
