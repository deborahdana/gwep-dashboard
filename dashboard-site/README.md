# Dashboard Site (Shareable Webpage)

This static site reads data from:

- `../GWEP/insights/weekly_kpi_dashboard.csv`
- `../GWEP/insights/weekly_channel_dashboard.csv`
- `../GWEP/insights/weekly_channel_budget_recommendations.csv`

## Local preview

From the repository root:

```bash
python3 -m http.server 8000
```

Then open:

- `http://localhost:8000/dashboard-site/`

## Publish to GitHub Pages

1. Push this project to your GitHub repo.
2. In GitHub, go to **Settings -> Pages**.
3. In "Build and deployment", choose:
   - **Source:** Deploy from a branch
   - **Branch:** `main`
   - **Folder:** `/dashboard-site`
4. Save, wait 1-2 minutes, then open your Pages URL.

## Keep dashboard updated

Each week:

1. Update files in `GWEP/insights/`.
2. Commit and push.
3. Refresh the Pages URL.
