# GWEP Growth Workspace

This folder stores marketing, funnel, and customer data for **GWEP Cumbres Herradura** — condo inventory + pre-construction in **Mexico City**.

**Best-in-class dashboard template (tiered KPIs, funnel, segmentation):** `analysis/BEST_IN_CLASS_WEEKLY_DASHBOARD_SPEC.md`

**Master checklist of what to add (data, CRM, process):** `analysis/DASHBOARD_IMPLEMENTATION_CHECKLIST.md`

## Recommended ingestion order

1. `data/paid_campaigns/paid_campaigns_master.csv`
2. `data/organic/organic_performance_master.csv`
3. `data/web/web_funnel_master.csv`
4. `data/leads/leads_master.csv`
5. `data/customers/customers_master.csv`

## Minimum KPI set

- Paid: spend, clicks, leads, CPL, CAC, ROAS
- Organic: reach, engagement, site visits, leads
- Web: sessions, conversion rate by step, source/medium
- Leads: source, stage, owner, created_at, converted_at, status
- Customers: close_date, revenue, source, campaign, product

## Update cadence

- Weekly: paid + organic + web
- Daily (if possible): leads
- Monthly: closed customers + revenue

## Weekly KPI dashboard

- Dashboard standard: `analysis/WEEKLY_KPI_DASHBOARD_STANDARD.md`
- Dashboard data table: `insights/weekly_kpi_dashboard.csv`
- Weekly update prompt: `analysis/WEEKLY_UPDATE_PROMPT.md`

## Weekly channel dashboard

- Channel standard: `analysis/WEEKLY_CHANNEL_DASHBOARD_STANDARD.md`
- Channel KPI table: `insights/weekly_channel_dashboard.csv`
- Budget recommendations table: `insights/weekly_channel_budget_recommendations.csv`
- Weekly channel prompt: `analysis/WEEKLY_CHANNEL_UPDATE_PROMPT.md`

## Notes

- Keep one row per natural grain (for example: per campaign/day, per lead, per customer).
- Use ISO dates (`YYYY-MM-DD`).
- Keep field names in snake_case.
