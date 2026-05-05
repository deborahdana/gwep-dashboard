# Weekly channel update prompt (copy/paste in chat)

Use this prompt weekly to decide budget allocation by channel:

---

Update my weekly channel dashboard and budget recommendations using:

- `GWEP/analysis/WEEKLY_CHANNEL_DASHBOARD_STANDARD.md`
- `GWEP/insights/weekly_channel_dashboard.csv`
- `GWEP/insights/weekly_channel_budget_recommendations.csv`
- `GWEP/data/paid_campaigns/paid_campaigns_master.csv`
- `GWEP/data/organic/organic_performance_master.csv`
- `GWEP/data/leads/leads_master.csv`
- `GWEP/data/customers/customers_master.csv`

Tasks:

1. Calculate weekly channel KPIs for at least `meta`, `google`, and `organic`.
2. Append/update channel rows in `GWEP/insights/weekly_channel_dashboard.csv`.
3. Compute channel scores (efficiency, quality, scale, total).
4. Recommend budget moves per channel:
   - increase_budget / keep_budget / decrease_budget / fix_tracking_first
5. Append/update `GWEP/insights/weekly_channel_budget_recommendations.csv`.
6. Explain where to move budget this week and estimated impact on leads and sales.
7. Flag attribution issues and missing fields.

---
