# Best-in-class weekly dashboard — GWEP Cumbres Herradura (CDMX condo)

This document is your **north-star template**. Build it in layers: ship Tier 1 first, then add Tier 2 when CRM hygiene supports it, then Tier 3 for forecasting and investor-grade reporting.

**Product context:** single complex, **pre-construction + inventory** units, Mexico City. Same brand and funnel, but **two commercial motions** that must be segmented or averages will mislead you.

---

## Design principles

1. **One weekly story:** what improved, what broke, what we change next week (budget + sales motion).
2. **Same definitions everywhere:** lead, qualified lead, visit, quote, reservation, contract, closed won.
3. **Segment or lie:** always split **pre-construction vs inventory** (and optionally tower/phase, typology, price band).
4. **Leading weekly, lagging monthly:** velocity and stage conversion weekly; true CAC/ROAS monthly once revenue is clean.
5. **Trust layer:** every week, note data gaps (missing source, mis-staged deals, duplicate leads).

---

## Weekly dashboard layout (recommended sections)

### A. Executive strip (always visible)

| Block | What it answers |
|--------|------------------|
| North star | Signed contracts / escrituras / cash-collected milestone you trust most (pick **one** primary). |
| Pipeline health | Count + MXN value in “hot” stages (visit scheduled → reservation intent). |
| Marketing efficiency | Blended CPL + **qualified CPL** (once defined). |
| Sales velocity | Median days lead → first visit; visit → reservation-related stage. |
| Alert | Top anomaly (e.g. show-rate drop, spike in “unassigned source”). |

### B. Demand generation (marketing)

**Spend & mix**

- Spend by channel: Meta, Google, YouTube, offline, partners/brokers, events.
- Share of spend vs share of **qualified** pipeline (not just leads).

**Funnel (media → CRM)**

- Impressions / reach / frequency (where relevant).
- CTR, LP sessions, form submit rate, cost per form.

**Quality**

- % leads with **budget + timeline + financing intent + product fit** (minimum qualification).
- Disposition reasons for rejects (optional early; powerful later).

### C. Pipeline & conversion (sales + CRM)

Use **stage conversion rates**, not only counts. For residential Mexico, typical stages map to your HubSpot reality (names may vary):

| Concept | Example CRM stages / checkpoints |
|--------|-----------------------------------|
| Capture | Nuevo / intento de contacto |
| Qualification | Contactado |
| Intent | Visita agendada |
| Commercial depth | Cotización / oferta |
| Commitment | Apartado / enganche-related milestones |
| Legal / closing | Documentación → escritura / entrega |

**Weekly must-have conversion KPIs**

- Lead → first meaningful contact (and **median hours**).
- Contact → visit held (**show rate**).
- Visit → formal quote/offer.
- Offer → apartado / reservation payment (your definition).
- Apartado → escritura / entrega (lagging; still track inflow weekly).

**Velocity**

- Median and p90 days for each transition above (by segment).

**Stale pipeline**

- Deals with **no activity** in 7 / 14 days (by stage).

### D. Product split: pre-construction vs inventory

Minimum segmentation (weekly):

| Dimension | Why |
|-----------|-----|
| **Product line** | Pre-construction vs inventory (different buyer urgency, financing, and cycle length). |
| **Unit typology** | Beds / m² band / tower or phase. |
| **Price band** | MXN band aligned to your price sheet. |

**KPIs to show side-by-side**

- Leads, qualified leads, visits, reservations-in-progress, closed (whatever definition you use).
- CPL and **cost per qualified lead** by segment when sample size allows.

### E. Channel & partner performance

- Paid social vs search vs organic vs referral vs broker **(if tracked)**.
- For each: leads, qualified rate, visit rate, **cost per visit** (best practice once visits are reliable).

### F. Inventory-specific block (operational)

Weekly operational clarity prevents marketing from promising what sales cannot fulfill.

- Available units (by typology).
- Units reserved / under contract / blocked.
- Average days on market for inventory units (if meaningful sample).

### G. Experiments & learning log (lightweight)

- 1–3 active tests (creative angle, audience, offer, landing page).
- Hypothesis, primary metric, end date, result so far.

---

## Tiered implementation (what to add when)

### Tier 1 — Foundation (you can run this month)

**Goal:** trustworthy weekly view of volume, spend, and basic funnel.

- Weekly spend by channel + **total leads** + **stage counts** from CRM export.
- CPL (blended) + simple qualification rule (even manual tag).
- Speed-to-first-contact (sample or median from CRM timestamps).
- Pre-construction vs inventory flag on every opportunity.

**Required CRM fields (minimum)**

- `product_line`: `pre_construction` | `inventory`
- `source` / `medium` / `campaign` (consistent taxonomy)
- `created_at`, `stage`, `owner`
- `first_contact_at`, `visit_scheduled_at`, `visit_held_at` (as soon as possible)

### Tier 2 — Best-in-class weekly operating rhythm

**Goal:** optimization-grade dashboard.

- Qualified lead definition enforced at capture (budget, timeline, financing, fit).
- Stage-to-stage conversion + **velocity** by segment.
- Show rate, stale pipeline, rep/closer workload.
- Cost per **visit** and cost per **qualified** lead by channel.

**Adds**

- Web funnel (`web_funnel_master.csv`) tied to UTMs.
- Organic social metrics tied to **sessions/leads** with UTMs or CRM campaign ID.

### Tier 3 — Commercial truth for NA / investors

**Goal:** ROI and forecasting.

- Revenue / deposits / payment schedule milestones by cohort.
- ROAS and payback windows by channel.
- Weighted pipeline forecast.

Requires finance-aligned definitions (IVA, payment timing, cancellations).

---

## Suggested future data files (optional; add as you grow)

Keep grain consistent; use `snake_case` and ISO dates.

| File | Grain | Purpose |
|------|--------|---------|
| `data/inventory/inventory_units_master.csv` | one row per unit | Stock, status, typology, list price, phase. |
| `data/funnel/stage_events.csv` | one row per stage transition | Precise velocity (best-in-class). |
| `data/marketing/campaign_map.csv` | campaign IDs ↔ product line | Clean attribution. |

Your existing `weekly_*_dashboard.csv` outputs remain the **weekly rollup layer**; detailed tables feed rollups via script (like `build_insights_from_data.py`).

---

## Weekly narrative template (copy/paste)

Use this every Monday for 10 minutes.

1. **Highlight:** The single best number this week (segment + channel).
2. **Concern:** The single worst trend (conversion or velocity).
3. **Marketing action:** One budget or creative move (with guardrails).
4. **Sales action:** One process fix (SLA, follow-up, visit confirmation).
5. **Data fix:** One field or taxonomy improvement for next week.

---

## Alignment with current repo artifacts

- Standards: `WEEKLY_KPI_DASHBOARD_STANDARD.md`, `WEEKLY_CHANNEL_DASHBOARD_STANDARD.md`
- Rollup builder: `build_insights_from_data.py` (extend when new sources exist)
- Live site: `docs/` (GitHub Pages)

Next logical upgrade: add **product_line** and **stage conversion** tables to the rollup script once those columns are stable in HubSpot exports.

---

## Gut-check before sharing externally

Extreme week-over-week swings often mean **taxonomy or tracking** changed, not performance. Validate the top 2–3 numbers that drive your narrative before presenting to leadership or partners.
