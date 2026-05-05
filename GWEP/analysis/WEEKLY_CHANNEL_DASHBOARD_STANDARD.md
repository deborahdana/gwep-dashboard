# Weekly Channel Dashboard Standard (GWEP Cumbres Herradura)

This dashboard compares weekly performance by channel and recommends budget shifts.

## Channels

Track at minimum:

- `meta`
- `google`
- `organic`

You can add more channels later (for example: `tiktok`, `linkedin`, `email`).

## Primary KPIs by channel

1. **Spend** (for paid channels)
2. **Leads**
3. **Qualified leads**
4. **New customers**
5. **Attributed revenue**
6. **CPL** = spend / leads
7. **CAC** = spend / new_customers
8. **Lead-to-Sale Rate** = new_customers / leads
9. **ROAS** = attributed_revenue / spend

## Decision framework (budget moves)

For each channel, score:

- **Efficiency score** (40%): CPL and CAC versus 4-week average
- **Quality score** (35%): lead-to-sale rate and qualified lead share
- **Scale score** (25%): available volume without major efficiency loss

Then recommend one of:

- `increase_budget`
- `keep_budget`
- `decrease_budget`
- `fix_tracking_first`

## Weekly output files

1. `GWEP/insights/weekly_channel_dashboard.csv`
2. `GWEP/insights/weekly_channel_budget_recommendations.csv`

## Data rules

- If spend is zero, keep CPL/CAC/ROAS blank.
- `organic` should have spend as 0 unless you are loading explicit content production cost.
- Use consistent attribution logic across channels each week.
- If attribution gaps are large, use `fix_tracking_first`.
