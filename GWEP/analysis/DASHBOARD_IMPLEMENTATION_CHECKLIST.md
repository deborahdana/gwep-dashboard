# Checklist — everything to add for the best-in-class GWEP dashboard

Use this as your master backlog. Mark items as you complete them. Full context and rationale live in **`BEST_IN_CLASS_WEEKLY_DASHBOARD_SPEC.md`**.

Legend: **T1** = Tier 1 foundation · **T2** = operating excellence · **T3** = commercial / investor grade

---

## 1. Governance and definitions (do this first)

- [ ] **T1** Pick one **north-star outcome** (e.g. escrituras, cash collected, or signed contract—document which).
- [ ] **T1** Write one-paragraph definitions for: *lead*, *qualified lead*, *visit (held)*, *quote/offer*, *apartado / reservation*, *closed won*.
- [ ] **T1** Agree **who owns** source taxonomy updates (marketing vs CRM admin).
- [ ] **T2** Document **disposition / lost reasons** (minimum list) for funnel exits.
- [ ] **T2** Weekly **data quality note** ritual (what broke in tracking this week).

---

## 2. CRM (HubSpot) — fields and hygiene

### Required for segmentation (CDMX condo, dual product line)

- [ ] **T1** **Product line** on every deal: `pre_construction` vs `inventory` (property or single-select).
- [ ] **T2** **Unit / typology** (beds, m² band, tower/phase, or link to unit ID).
- [ ] **T2** **Price band** (aligned to your price list).
- [ ] **T2** **Buyer intent** (e.g. end user vs investor vs relocation) if you will market differently.

### Source and attribution

- [ ] **T1** Consistent **source / medium / campaign** (UTM or campaign ID) on web leads; **enforcement** on forms.
- [ ] **T2** **Last-touch vs first-touch** rule documented (pick one for weekly dashboard).
- [ ] **T2** **Broker / partner** source vs paid vs organic clearly labeled.
- [ ] **T2** Rules for **“sin conexión” / unknown source** cleanup (reduce bucket size over time).

### Timestamps for velocity (critical for best-in-class)

- [ ] **T1** **Lead created date** (already typical).
- [ ] **T1** **First meaningful contact** datetime (or date entered “Contactado”).
- [ ] **T2** **Visit scheduled** and **visit held** (actual appointment—not only stage name).
- [ ] **T2** **Quote / offer sent** milestone (cotización / oferta).
- [ ] **T2** **Apartado / reservation / enganche** milestones matching your legal/commercial reality.
- [ ] **T3** **Escritura / entrega** (or your closing milestone).

### Qualification (quality KPIs)

- [ ] **T1** **Budget range** (or min down payment).
- [ ] **T1** **Purchase timeline** (e.g. 0–3 / 3–6 / 6+ months).
- [ ] **T1** **Financing intent** (infonavit, banco, contado, mix).
- [ ] **T1** **Product fit** (inventory vs pre-construction interest, typology).
- [ ] **T2** **Computed “qualified” flag** or score from the fields above (single rule everyone uses).

### Pipeline health

- [ ] **T1** Stage model matches weekly dashboard stages (no orphan stages).
- [ ] **T2** **Last activity date** + automation/stale alerts (7 / 14 days).
- [ ] **T2** **Owner** on every open deal; reassignment rules.

---

## 3. Marketing and paid media data

- [ ] **T1** Weekly **Meta spend** (account/campaign level export or cohort rollup—you already use cohort-style reporting).
- [ ] **T1** Weekly **Google Ads spend** (same).
- [ ] **T2** **YouTube / other paid** if active (even monthly at first).
- [ ] **T2** **Offline / events / partners** spend log (simple spreadsheet if small).
- [ ] **T2** **Impressions, clicks, CTR** by major campaign (for creative learning).
- [ ] **T2** **Cost per form submit** and **LP conversion** where landing pages exist.
- [ ] **T3** **Cost per qualified lead** and **cost per visit** by channel (needs CRM fields above).

---

## 4. Organic, content, and web

- [ ] **T1** **GA4** (or similar) on site: sessions, key events (form, click-to-call, WhatsApp).
- [ ] **T1** `web_funnel_master.csv` (or live export) with **UTM** and key steps filled weekly.
- [ ] **T2** **Meta / IG** (and others) exports: reach, engagement, saves—**tied to tracked links** where possible.
- [ ] **T2** **Content → lead** mapping (post ID or campaign param to CRM).
- [ ] **T2** **Brand / non-paid** leads separated from paid in reporting.

---

## 5. Inventory and product (condo-specific)

- [ ] **T2** **Inventory master**: one row per unit (ID, typology, status, list price, phase/tower).
- [ ] **T2** **Weekly snapshot** of available / reserved / blocked (can be a simple weekly CSV at first).
- [ ] **T2** **Pre-construction** release schedule (towers/phases) for marketing alignment.
- [ ] **T3** **Days on market** for inventory units (needs status change dates).

Optional file (see spec): `GWEP/data/inventory/inventory_units_master.csv` (when ready).

---

## 6. Finance and commercial truth (Tier 3)

- [ ] **T3** **Deal value** and **payment structure** (enganche, monthly, schedule) in CRM or finance export.
- [ ] **T3** **Revenue recognition rules** (what counts as “closed” for ROAS).
- [ ] **T3** **Cancellations / refunds** tracked so cohorts are honest.
- [ ] **T3** **ROAS / payback** by channel (monthly at minimum).

---

## 7. Experiments and learning

- [ ] **T2** Simple **experiments log**: hypothesis, start/end, primary metric, result (sheet or markdown).
- [ ] **T2** **Creative naming** convention (angle, offer, audience) in ad platforms.

---

## 8. Dashboard stack (technical — many items already in place)

- [x] **T1** Weekly rollup CSVs + script: `GWEP/analysis/build_insights_from_data.py`
- [x] **T1** GitHub Pages site under `docs/` with synced `docs/insights/*.csv`
- [ ] **T1** When data changes: run script → commit → push (documented in `docs/README.md`)
- [ ] **T2** Extend script or add scripts for **product_line** and **stage conversion** once CRM exports include fields.
- [ ] **T2** Optional: **stage transition** file (`stage_events`) for precise velocity.
- [ ] **T2** HTML dashboard: new sections for **executive strip**, **pre-construction vs inventory**, **funnel conversion** (incremental UI work).

---

## 9. Operating rhythm (not data, but required for “best in class”)

- [ ] **T1** Weekly 30-minute **metrics review** (same weekday, same agenda).
- [ ] **T1** One **marketing action** and one **sales action** recorded each week.
- [ ] **T2** Monthly **definition / taxonomy** retro (30 min).

---

## Suggested order (minimize thrash)

1. Definitions + **product_line** + **source taxonomy** + **qualification fields** (Section 1–2).
2. **Spend + CRM export** weekly discipline (Section 3).
3. **Web / UTMs** (Section 4).
4. **Velocity timestamps** and **visits** (Section 2).
5. **Inventory master** (Section 5).
6. **Finance linkage** (Section 6).
7. **UI sections** on the live dashboard as each block has stable data (Section 8).

---

When in doubt, validate the **2–3 numbers** that drive your weekly story before making big budget or board-level claims.
