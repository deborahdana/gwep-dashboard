# Dashboard Site (Shareable Webpage)

This static site reads CSV from **`docs/insights/`** (copied from `GWEP/insights/` so GitHub Pages can load them from the same origin). After updating weekly KPI files under `GWEP/insights/`, copy them into `docs/insights/` and push.

Files:

- `insights/weekly_kpi_dashboard.csv`
- `insights/weekly_channel_dashboard.csv`
- `insights/weekly_channel_budget_recommendations.csv`

## Local preview

From the repository root:

```bash
python3 -m http.server 8000
```

Then open:

- `http://localhost:8000/docs/`

GitHub Pages only supports publishing from **`/` (root)** or **`/docs`**. This site lives in **`docs/`** so you choose **`/docs`** in Pages settings—not a custom folder name like `dashboard-site`.

## Publish to GitHub Pages

1. Push this project to your GitHub repo.
2. In GitHub, go to **Settings -> Pages**.
3. In "Build and deployment", choose:
   - **Source:** Deploy from a branch
   - **Branch:** `main`
   - **Folder:** `/docs`
4. Save, wait 1-2 minutes, then open your Pages URL (for project repos: `https://<user>.github.io/<repo>/`).

## Keep dashboard updated

Each week:

1. Update files in `GWEP/insights/`.
2. Commit and push.
3. Refresh the Pages URL.
