# Weekly KPI Dashboard Standard (GWEP Cumbres Herradura)

This standard defines the weekly dashboard your agent should update every week.

## KPI definitions (official)

1. **CPL (Cost per Lead)** = total_paid_spend / total_leads
2. **CAC (Customer Acquisition Cost)** = total_paid_spend / new_customers
3. **Lead-to-Sale Rate** = new_customers / total_leads
4. **ROAS (Return on Ad Spend)** = attributed_revenue / total_paid_spend
5. **Closing Velocity (days)** = average(close_date - lead_created_at) for closed-won customers

## Weekly grain

Use one row per week in `GWEP/insights/weekly_kpi_dashboard.csv`.

- `week_start`: Monday date (`YYYY-MM-DD`)
- `week_end`: Sunday date (`YYYY-MM-DD`)

## Source mapping

- `total_paid_spend`, `total_leads`:
  - from `GWEP/data/paid_campaigns/paid_campaigns_master.csv`
- `new_customers`, `attributed_revenue`:
  - from `GWEP/data/customers/customers_master.csv`
- `lead_created_at`, funnel status:
  - from `GWEP/data/leads/leads_master.csv`

## Data quality rules

- If denominator is zero, set KPI as blank (not 0) and flag in `notes`.
- Keep currency consistent week over week.
- Only count `status=won` as customer sales.
- If attribution is mixed, use last-touch by default and note that in `notes`.

## Weekly output format

Every weekly dashboard update should include:

1. KPI table updated in `GWEP/insights/weekly_kpi_dashboard.csv`
2. 3-bullet interpretation:
   - what improved
   - what declined
   - most likely reason
3. 3 actions for next week with expected impact

## KPI targets (initial)

Update these once you have 6-8 weeks of real history.

- CPL target: <= 10% lower than 4-week average
- CAC target: <= 10% lower than 4-week average
- Lead-to-Sale target: >= 10% above 4-week average
- ROAS target: >= 15% above 4-week average
- Closing Velocity target: <= 10% faster than 4-week average
