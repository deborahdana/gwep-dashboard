# Checklist — everything to add for the best-in-class GWEP dashboard

Use this as your master backlog. Mark items as you complete them. Full strategic context lives in **`BEST_IN_CLASS_WEEKLY_DASHBOARD_SPEC.md`**.

Legend: **T1** = Tier 1 foundation (start here) · **T2** = operating excellence · **T3** = commercial / investor grade

**How to read each item:** Every checkbox below has *Plain English*, *Why it matters*, and *Practical step / Done when* so nothing stays abstract.

---

## 1. Governance and definitions (do this first)

### North star

- [ ] **T1** Pick one **north-star outcome** (e.g. escrituras, cash collected, or signed contract—document which).

  - **Plain English:** Pick the **one number** that means “we won” for your business this quarter—not ten competing KPIs.
  - **Why it matters:** If everyone optimizes a different number, marketing celebrates CPL while sales misses escrituras. One anchor keeps teams aligned.
  - **Done when:** Written in one sentence (“Our north star for QX is ___ because ___”) and shared with marketing + sales.

---

### Shared definitions

- [ ] **T1** Write one-paragraph definitions for: *lead*, *qualified lead*, *visit (held)*, *quote/offer*, *apartado / reservation*, *closed won*.

  - **Plain English:** A mini playbook so nobody argues about labels—“we only count a visit when ___.”
  - **Why it matters:** Dashboard percentages change overnight when definitions drift; you stop trusting week-over-week trends.
  - **Done when:** A half-page doc exists and CRM stages/property names match those definitions as closely as possible.

---

### Who owns names (taxonomy)

- [ ] **T1** Agree **who owns** source taxonomy updates (marketing vs CRM admin).

  - **Plain English:** Decide **who is allowed to invent or rename** lead sources and campaigns (the words that show up in CRM and exports).
  - **Why it matters:** If ads change names weekly but CRM picklists don’t, you get duplicates, “unknown,” and wrong CPL by channel—without anyone misbehaving on purpose.
  - **Practical rule that works:** Marketing owns **meaning** (“these are our channels/campaigns”). CRM admin owns **implementation** (dropdowns, required fields, workflows). Changes go through one lightweight approval so exports stay stable.
  - **Done when:** Names written down + one owner + backup (people, not “the team”).

---

### Why deals exit (lost reasons)

- [ ] **T2** Document **disposition / lost reasons** (minimum list) for funnel exits.

  - **Plain English:** When someone **does not buy**, capture **why** using a **short picklist** (plus optional comment)—not only free text.
  - **Why it matters:** Conversion tells you *that* you lost; reasons tell you *where to fix* (creative vs pricing vs inventory vs financing vs competitor).
  - **Starter list to tailor:** budget fit · financing · timeline · unit not available · chose competitor · location/commute · ghosted/no response · duplicate/test · other (specify).
  - **Done when:** HubSpot (or CRM) requires or strongly encourages picklist on closed-lost/disqualified; monthly review of top three reasons by source.

---

### Weekly “truth in advertising” note

- [ ] **T2** Weekly **data quality note** ritual (what broke in tracking this week).

  - **Plain English:** Every week, write **a few honest bullets** about anything that could make this week’s numbers lie (bugs, missing UTMs, form downtime, pipeline renamed, etc.).
  - **Why it matters:** Otherwise you react to **noise** (broken tracking) as if it were **performance**.
  - **Examples of good notes:** “Meta pixel fired twice Thu—duplicate events.” “New LP shipped without UTMs Tue–Wed.” “CRM merge deduped 40 records—counts may drop.”
  - **Done when:** Same place every week (tab in a sheet, Slack template, or `notes` when you regenerate CSVs) + 5 minutes every Monday.

---

## 2. CRM (HubSpot) — fields and hygiene

### Required for segmentation (CDMX condo, dual product line)

- [ ] **T1** **Product line** on every deal: `pre_construction` vs `inventory` (property or single-select).

  - **Plain English:** Tag every opportunity as **inventory you can close soon** vs **pre-construction / future delivery**—whatever matches how you actually sell.
  - **Why it matters:** Same CPL can hide opposite stories (investors vs families, urgency vs long funnel). Blended averages mislead.
  - **Done when:** Field is required before deal moves past early stage (or enforced via automation), and exports include it.

- [ ] **T2** **Unit / typology** (beds, m² band, tower/phase, or link to unit ID).

  - **Plain English:** What **kind of home** they want or what unit they’re tied to—bedrooms, size bucket, tower/phase if your project uses those.
  - **Why it matters:** Creative and budget rotate by typology; “we need more leads” might mean “we need more 2-bed buyers,” not more raw forms.
  - **Done when:** Filterable on dashboards and used in at least one weekly discussion (“which typology fed visits this week?”).

- [ ] **T2** **Price band** (aligned to your price list).

  - **Plain English:** Bucket price into bands you actually use in meetings (e.g. entry vs premium within the development).
  - **Why it matters:** Separates tire-kickers from serious buyers when CPL looks fine but quality isn’t.
  - **Done when:** Bands documented next to your official price sheet so marketing and sales use the same bins.

- [ ] **T2** **Buyer intent** (e.g. end user vs investor vs relocation) if you will market differently.

  - **Plain English:** **Who they are buying for** and **why now**—even a simple dropdown.
  - **Why it matters:** Messaging and channels differ; mixing intents inflates CPL on campaigns aimed at only one group.
  - **Done when:** Used at least once to pause or scale a campaign based on intent mix.

---

### Source and attribution

- [ ] **T1** Consistent **source / medium / campaign** (UTM or campaign ID) on web leads; **enforcement** on forms.

  - **Plain English:** Every web lead should arrive with **readable labels** that match your taxonomy (where they came from and which campaign).
  - **Why it matters:** Without UTMs/hidden fields, everything lands in “direct” or “offline”—you cannot optimize spend honestly.
  - **Done when:** Forms pass UTMs; quarterly audit shows **low** “unknown source” share.

- [ ] **T2** **Last-touch vs first-touch** rule documented (pick one for weekly dashboard).

  - **Plain English:** Decide whether credit goes to **what touched them last** or **what discovered them first**—then stick to it for weekly reporting.
  - **Why it matters:** Same lead journey gets different answers; teams argue without a written rule.
  - **Done when:** One paragraph in your playbook + reflected in how you pull HubSpot reports.

- [ ] **T2** **Broker / partner** source vs paid vs organic clearly labeled.

  - **Plain English:** When a broker brings a buyer, it should **never** look identical to a Meta lead in exports.
  - **Why it matters:** Partner economics differ (commissions); mixing them breaks CPL and ROI math.
  - **Done when:** Broker-led deals have their own source path or deal property everyone uses.

- [ ] **T2** Rules for **“sin conexión” / unknown source** cleanup (reduce bucket size over time).

  - **Plain English:** “Unknown” is a **to-do list**, not a permanent bucket—rules for how ops fixes legacy or messy leads weekly.
  - **Why it matters:** Unknown grows until half your pipeline is unactionable for attribution.
  - **Done when:** Owner + weekly cap (“we clear top 20 unknowns” or “unknown below X%”).

---

### Timestamps for velocity (critical for best-in-class)

- [ ] **T1** **Lead created date** (already typical).

  - **Plain English:** When they **first entered** your world (form, call, walk-in logged as lead).
  - **Why it matters:** Start of the clock for speed-to-lead and funnel aging.
  - **Done when:** Always populated automatically; never hand-edited except error correction.

- [ ] **T1** **First meaningful contact** datetime (or date entered “Contactado”).

  - **Plain English:** When your team **actually reached** them—not when marketing paid for the click.
  - **Why it matters:** Measures sales responsiveness and handoff quality.
  - **Done when:** Used in at least one weekly SLA (“median hours to first touch”).

- [ ] **T2** **Visit scheduled** and **visit held** (actual appointment—not only stage name).

  - **Plain English:** **Booked** vs **happened**—two different ideas (show rate lives here).
  - **Why it matters:** Many “visits” in CRM are hopeful; best-in-class tracks **held** visits for truth.
  - **Done when:** You report show rate weekly when sample size allows.

- [ ] **T2** **Quote / offer sent** milestone (cotización / oferta).

  - **Plain English:** When they received **numbers they can decide on** (formal quote or offer package—your legal/commercial definition).
  - **Why it matters:** Separates tire-kickers from real consideration; feeds conversion after visit.
  - **Done when:** Date captured once per deal when quote goes out.

- [ ] **T2** **Apartado / reservation / enganche** milestones matching your legal/commercial reality.

  - **Plain English:** When money or commitment **materializes** the way your contracts use those words in Mexico.
  - **Why it matters:** Marketing “leads” stop mattering here—this is where cash and forecast begin.
  - **Done when:** Finance and legal agree on which CRM milestone equals “we have real commitment” for reporting.

- [ ] **T3** **Escritura / entrega** (or your closing milestone).

  - **Plain English:** When the deal is **legally / economically closed** the way your board counts it.
  - **Why it matters:** ROAS and payback tie to this—not to leads.
  - **Done when:** Can tie back to original campaign/source for winner analysis (even roughly).

---

### Qualification (quality KPIs)

- [ ] **T1** **Budget range** (or min down payment).

  - **Plain English:** What they can **actually pay** or put down—not “I’ll figure it out later.”
  - **Why it matters:** Stops optimizing ads for people who cannot buy your band.
  - **Done when:** Collected at first serious qualification call or form step.

- [ ] **T1** **Purchase timeline** (e.g. 0–3 / 3–6 / 6+ months).

  - **Plain English:** **When** they intend to decide or close—rough buckets are fine.
  - **Why it matters:** Pre-construction vs inventory urgency differs; nurture length differs.
  - **Done when:** Used to prioritize callbacks within 24–48h.

- [ ] **T1** **Financing intent** (infonavit, banco, contado, mix).

  - **Plain English:** **How** they plan to pay—mortgage path vs cash vs mix.
  - **Why it matters:** Creative and objection handling change; financing drops are a leading indicator.
  - **Done when:** Sales uses it in discovery checklist every time.

- [ ] **T1** **Product fit** (inventory vs pre-construction interest, typology).

  - **Plain English:** Whether what you sell **matches** what they want (product line + rough unit size).
  - **Why it matters:** High CPL with wrong fit is a positioning problem, not a volume problem.
  - **Done when:** Reported as **mismatch rate** when leads spike.

- [ ] **T2** **Computed “qualified” flag** or score from the fields above (single rule everyone uses).

  - **Plain English:** One **transparent rule** everyone agrees on (“qualified = budget + timeline + financing + fit”).
  - **Why it matters:** Stops endless debates about “quality” in meetings.
  - **Done when:** Formula written down and recomputed in HubSpot or in your rollup script.

---

### Pipeline health

- [ ] **T1** Stage model matches weekly dashboard stages (no orphan stages).

  - **Plain English:** CRM stages **map cleanly** to how you read the funnel in the weekly meeting—no mystery stages nobody uses.
  - **Why it matters:** Orphan stages break conversion math and confuse reps.
  - **Done when:** Diagram of stages matches HubSpot and your dashboard doc.

- [ ] **T2** **Last activity date** + automation/stale alerts (7 / 14 days).

  - **Plain English:** Know when a deal **went quiet** so nobody hides stagnation.
  - **Why it matters:** Inventory moves fast; silence equals leakage or fear of closing lost.
  - **Done when:** Weekly count of “stale” deals by stage appears in your ritual.

- [ ] **T2** **Owner** on every open deal; reassignment rules.

  - **Plain English:** **Someone’s name** is on every live opportunity; clear rules when it changes hands.
  - **Why it matters:** Unowned pipeline inflates lead counts and hides accountability.
  - **Done when:** Zero “unassigned” in open pipeline except a defined triage queue.

---

## 3. Marketing and paid media data

- [ ] **T1** Weekly **Meta spend** (account/campaign level export or cohort rollup—you already use cohort-style reporting).

  - **Plain English:** **How much money** went to Facebook/Instagram ads this week—same currency and week boundaries every time.
  - **Why it matters:** CPL and ROAS are meaningless if spend weeks don’t match CRM weeks.
  - **Done when:** Same calendar definition as your cohort or CRM weekly export.

- [ ] **T1** Weekly **Google Ads spend** (same).

  - **Plain English:** Same as Meta, for Search/Display/YouTube if grouped under Google Ads billing.
  - **Why it matters:** Search intent often out-converts social when tracked separately.
  - **Done when:** Can compare Meta vs Google apples-to-apples weekly.

- [ ] **T2** **YouTube / other paid** if active (even monthly at first).

  - **Plain English:** Any **other paid line items** that aren’t only Meta/Google (portals, radio, etc.).
  - **Why it matters:** Hidden spend makes blended CPL look better than reality.
  - **Done when:** One tab or row in your weekly money log.

- [ ] **T2** **Offline / events / partners** spend log (simple spreadsheet if small).

  - **Plain English:** Cake-and-coffee events, booth fees, partner programs—**money out** even if not “digital.”
  - **Why it matters:** Otherwise organic looks magical and paid looks guilty.
  - **Done when:** Event cost per lead becomes discussable (even rough).

- [ ] **T2** **Impressions, clicks, CTR** by major campaign (for creative learning).

  - **Plain English:** **Reach and attention** before leads—are people seeing and clicking the right story?
  - **Why it matters:** Separates **message fatigue** from **CRM problems** when leads drop.
  - **Done when:** Top 3 campaigns each week get one sentence (“CTR up—creative winning”).

- [ ] **T2** **Cost per form submit** and **LP conversion** where landing pages exist.

  - **Plain English:** Cost per **completed form** on the landing page vs overall CPL from CRM (they differ when leads leak).
  - **Why it matters:** Diagnoses broken forms vs bad traffic.
  - **Done when:** GA4 events or ad-platform conversions reconciled monthly.

- [ ] **T3** **Cost per qualified lead** and **cost per visit** by channel (needs CRM fields above).

  - **Plain English:** Spend divided by **qualified** leads and by **real visits**, not raw forms only.
  - **Why it matters:** Best-in-class optimizes quality and appointments, not cheap junk leads.
  - **Done when:** Marketing can defend budget with **cost per visit**, not only CPL.

---

## 4. Organic, content, and web

- [ ] **T1** **GA4** (or similar) on site: sessions, key events (form, click-to-call, WhatsApp).

  - **Plain English:** See **what people do on your website** after they click an ad or search you.
  - **Why it matters:** Separates “bad ads” from “bad site” when conversion tanks.
  - **Done when:** Key events fire reliably on thank-you / WhatsApp clicks.

- [ ] **T1** `web_funnel_master.csv` (or live export) with **UTM** and key steps filled weekly.

  - **Plain English:** A simple weekly table: sessions → key steps → submits, **tagged by campaign**.
  - **Why it matters:** Connects marketing storytelling to on-site behavior without digging GA every time.
  - **Done when:** Someone fills it every Monday in <15 minutes or automates export.

- [ ] **T2** **Meta / IG** (and others) exports: reach, engagement, saves—**tied to tracked links** where possible.

  - **Plain English:** Social **does not only mean followers**—it means measurable paths into CRM (links with UTMs, tracked phone/WhatsApp).
  - **Why it matters:** Vanity metrics feel good; tracked pipeline pays commissions.
  - **Done when:** At least one post type weekly ties to lead volume or sessions.

- [ ] **T2** **Content → lead** mapping (post ID or campaign param to CRM).

  - **Plain English:** When a lead says “I saw your Reel,” CRM still knows **which asset** helped (via UTM or hidden field).
  - **Why it matters:** Lets you double down on hooks that actually sell appointments.
  - **Done when:** Monthly “top content by assisted leads” becomes possible.

- [ ] **T2** **Brand / non-paid** leads separated from paid in reporting.

  - **Plain English:** People who find you **without that week’s ad spend** still matter—label them clearly.
  - **Why it matters:** Stops turning off paid when brand search was doing the real close.
  - **Done when:** Organic/direct buckets reviewed beside paid weekly.

---

## 5. Inventory and product (condo-specific)

- [ ] **T2** **Inventory master**: one row per unit (ID, typology, status, list price, phase/tower).

  - **Plain English:** A **single spreadsheet truth** for every unit: available, reserved, sold, hold—what it is and what it costs.
  - **Why it matters:** Marketing cannot advertise units sales cannot fulfill; dashboards cannot show real velocity without stock truth.
  - **Done when:** Weekly snapshot pulled from same file ops trusts.

- [ ] **T2** **Weekly snapshot** of available / reserved / blocked (can be a simple weekly CSV at first).

  - **Plain English:** Same inventory cut **every Monday** so trends mean something.
  - **Why it matters:** Daily noise makes weekly marketing decisions chaotic.
  - **Done when:** One dated export archived weekly (even manual).

- [ ] **T2** **Pre-construction** release schedule (towers/phases) for marketing alignment.

  - **Plain English:** When **which inventory** officially launches or opens for sale—dates that sales and marketing share.
  - **Why it matters:** Pre-sales campaigns must align with legal release and construction narrative.
  - **Done when:** Campaign calendar references phase dates explicitly.

- [ ] **T3** **Days on market** for inventory units (needs status change dates).

  - **Plain English:** How long **available** units sit before reservation—per typology if possible.
  - **Why it matters:** Separates demand problems from pricing problems.
  - **Done when:** Average DOM reviewed monthly when sample size exists.

Optional file (see spec): `GWEP/data/inventory/inventory_units_master.csv` (when ready).

---

## 6. Finance and commercial truth (Tier 3)

- [ ] **T3** **Deal value** and **payment structure** (enganche, monthly, schedule) in CRM or finance export.

  - **Plain English:** What they **owe and when**—not just list price.
  - **Why it matters:** Cash timing beats vanity pipeline for survival and ROAS honesty.
  - **Done when:** Finance accepts CRM or sheet as directional truth for weekly forecast.

- [ ] **T3** **Revenue recognition rules** (what counts as “closed” for ROAS).

  - **Plain English:** Written rule: ROAS uses **deposit**, **contract**, or **cash received**—pick one primary for marketing accountability.
  - **Why it matters:** Everyone stops arguing about “fake ROI.”
  - **Done when:** Document signed off by finance + leadership.

- [ ] **T3** **Cancellations / refunds** tracked so cohorts are honest.

  - **Plain English:** When deals **unwind**, mark them so past months’ wins aren’t overstated.
  - **Why it matters:** Otherwise you celebrate cohorts that collapse next quarter.
  - **Done when:** Monthly adjustment row or field exists (“net of cancel”).

- [ ] **T3** **ROAS / payback** by channel (monthly at minimum).

  - **Plain English:** **Marketing spend vs money back** over time—usually monthly, not noisy weekly.
  - **Why it matters:** Board-level and investor conversations require money truth, not CPL alone.
  - **Done when:** Simple chart: spend vs recognized revenue by channel with defined lag.

---

## 7. Experiments and learning

- [ ] **T2** Simple **experiments log**: hypothesis, start/end, primary metric, result (sheet or markdown).

  - **Plain English:** When you try a new hook or landing page, write **what you believed would happen** and **what did**—even one row.
  - **Why it matters:** Stops repeating failed tests and institutionalizes learning.
  - **Done when:** Every active test has an owner and end date.

- [ ] **T2** **Creative naming** convention (angle, offer, audience) in ad platforms.

  - **Plain English:** Ads named so a stranger can tell **angle + audience + offer** without opening the creative.
  - **Why it matters:** Downstream reporting becomes readable in Excel and CRM.
  - **Done when:** New campaigns follow pattern for 30 days straight.

---

## 8. Dashboard stack (technical — many items already in place)

- [x] **T1** Weekly rollup CSVs + script: `GWEP/analysis/build_insights_from_data.py`

  - **Plain English:** Code that turns raw exports into **dashboard-ready tables** so you don’t hand-merge Excel weekly forever.
  - **Done when:** You can regenerate insights after dropping new files in `GWEP/data/`.

- [x] **T1** GitHub Pages site under `docs/` with synced `docs/insights/*.csv`

  - **Plain English:** A **shareable URL** that reads your weekly CSVs—your live report.
  - **Done when:** Stakeholders open the link without logging into HubSpot.

- [ ] **T1** When data changes: run script → commit → push (documented in `docs/README.md`)

  - **Plain English:** Your **publish ritual**: update data → run Python → push GitHub → refresh browser.
  - **Why it matters:** The live site only updates when CSVs in `docs/insights/` update.
  - **Done when:** You’ve done it twice without help.

- [ ] **T2** Extend script or add scripts for **product_line** and **stage conversion** once CRM exports include fields.

  - **Plain English:** Next version of automation: split **pre-construction vs inventory** and stage-to-stage rates when columns exist.
  - **Done when:** New columns appear in HubSpot export and script maps them.

- [ ] **T2** Optional: **stage transition** file (`stage_events`) for precise velocity.

  - **Plain English:** One row every time a deal **changes stage**—best accuracy for “how many days in stage X.”
  - **Why it matters:** Stage-enter dates in HubSpot help, but event logs are clearest at scale.
  - **Done when:** Export or workflow writes transitions weekly.

- [ ] **T2** HTML dashboard: new sections for **executive strip**, **pre-construction vs inventory**, **funnel conversion** (incremental UI work).

  - **Plain English:** The **pretty front end** catches up as data becomes trustworthy—add sections one at a time.
  - **Done when:** Each new section has an owner and ships after its data field is stable for 2–4 weeks.

---

## 9. Operating rhythm (not data, but required for “best in class”)

- [ ] **T1** Weekly 30-minute **metrics review** (same weekday, same agenda).

  - **Plain English:** Same meeting, same clock, same three questions: what moved, why, what we do next week.
  - **Why it matters:** Dashboards without ritual become wallpaper.
  - **Done when:** Calendar invite exists + agenda doc.

- [ ] **T1** One **marketing action** and one **sales action** recorded each week.

  - **Plain English:** Leave every weekly meeting with **two concrete behaviors** changing—not only commentary.
  - **Why it matters:** Turns insight into throughput.
  - **Done when:** Written in notes (“marketing: ___”, “sales: ___”).

- [ ] **T2** Monthly **definition / taxonomy** retro (30 min).

  - **Plain English:** Once a month, ask “did any label or stage change confuse us?” and fix small drift before it rots data.
  - **Why it matters:** Prevents silent rewrites that break historical comparisons.
  - **Done when:** Four retros completed—adjust checklist if needed.

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
