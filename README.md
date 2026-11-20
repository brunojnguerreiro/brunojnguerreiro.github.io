# brunojnguerreiro.github.io

Source of https://brunojnguerreiro.github.io, built with [Pelican](https://getpelican.com).

- Edit pages in `content/pages/` (Markdown).
- Preview locally: `pip install -r requirements.txt && make devserver`, then open http://localhost:8000
- Publishing is automatic: every push to `main` builds and deploys the site via GitHub Actions
  (`.github/workflows/pages.yml`). In the repository settings, Pages → Source must be "GitHub Actions".
