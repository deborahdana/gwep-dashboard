#!/usr/bin/env python3
"""
Rebuild GWEP dashboard CSVs from:
- cohort_semanal_ch...csv (weekly leads, Meta/Google spend, ganado)
- leads/todos-negocios.csv (organic lead counts per cohort week window)

Run from repo root:
  python3 GWEP/analysis/build_insights_from_data.py

Writes:
  GWEP/insights/weekly_kpi_dashboard.csv
  GWEP/insights/weekly_channel_dashboard.csv
  GWEP/insights/weekly_channel_budget_recommendations.csv
  docs/insights/*.csv (same copies for GitHub Pages)
"""

from __future__ import annotations

import csv
import re
import shutil
from collections import defaultdict
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DATA = REPO / "GWEP" / "data"
INSIGHTS = REPO / "GWEP" / "insights"
DOCS_INSIGHTS = REPO / "docs" / "insights"

COHORT_FILE = DATA / "paid_campaigns" / "cohort_semanal_ch.xlsx - Reporte Semanal.csv"
LEADS_FILE = DATA / "leads" / "todos-negocios.csv"

ORGANIC_SOURCES = {
    "Tráfico orgánico de redes sociales",
    "Búsqueda orgánica",
}


def parse_mx_money(s: str) -> float:
    if not s or not str(s).strip():
        return 0.0
    s = str(s).strip().replace("$", "").replace(".", "").replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return 0.0


def parse_int_field(s: str) -> int:
    if not s or not str(s).strip():
        return 0
    try:
        return int(float(str(s).strip()))
    except ValueError:
        return 0


def sem_label_to_dates(label: str) -> tuple[datetime | None, datetime | None]:
    m = re.search(r"\((\d{1,2} \w{3}) - (\d{1,2} \w{3} (\d{4}))\)", label)
    if not m:
        return None, None
    start = datetime.strptime(f"{m.group(1)} {m.group(3)}", "%d %b %Y")
    end = datetime.strptime(m.group(2), "%d %b %Y")
    return start, end


def load_cohort_weeks() -> list[dict]:
    text = COHORT_FILE.read_text(encoding="utf-8")
    rows_out: list[dict] = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("Sem ") or "(" not in line:
            continue
        row = next(csv.reader([line]))
        if len(row) < 18:
            continue
        label = row[0].strip()
        total_leads = parse_int_field(row[1])
        contactado = parse_int_field(row[4])
        visita = parse_int_field(row[6])
        cotizacion = parse_int_field(row[8])
        apartado = parse_int_field(row[10])
        ganado = parse_int_field(row[12])
        perdido = parse_int_field(row[14])
        meta = parse_mx_money(row[16])
        google = parse_mx_money(row[17])
        spend = meta + google
        start, end = sem_label_to_dates(label)
        if start is None or end is None:
            continue
        qualified_proxy = contactado + visita + cotizacion + apartado
        rows_out.append(
            {
                "label": label,
                "week_start": start.date().isoformat(),
                "week_end": end.date().isoformat(),
                "total_leads": total_leads,
                "contactado": contactado,
                "qualified_proxy": qualified_proxy,
                "ganado": ganado,
                "meta_spend": meta,
                "google_spend": google,
                "total_spend": spend,
            }
        )
    rows_out.sort(key=lambda r: r["week_end"])
    return rows_out


def load_organic_counts_by_week(cohort_weeks: list[dict]) -> dict[tuple[str, str], int]:
    """Count HubSpot leads per cohort window where source is organic."""
    counts: dict[tuple[str, str], int] = defaultdict(int)
    if not LEADS_FILE.exists():
        return counts

    windows = [(w["week_start"], w["week_end"]) for w in cohort_weeks]

    def window_for(ts: datetime) -> tuple[str, str] | None:
        d = ts.date()
        for ws, we in windows:
            if datetime.strptime(ws, "%Y-%m-%d").date() <= d <= datetime.strptime(we, "%Y-%m-%d").date():
                return (ws, we)
        return None

    with LEADS_FILE.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            src = (row.get("Fuente original de tráfico") or "").strip()
            if src not in ORGANIC_SOURCES:
                continue
            raw = row.get("Fecha de creación") or ""
            raw = raw.strip()
            if not raw:
                continue
            # "2026-05-05 12:05"
            try:
                ts = datetime.strptime(raw[:16], "%Y-%m-%d %H:%M")
            except ValueError:
                try:
                    ts = datetime.strptime(raw[:10], "%Y-%m-%d")
                except ValueError:
                    continue
            wk = window_for(ts)
            if wk:
                counts[wk] += 1
    return counts


def fmt_float(x: float | None, nd: int = 4) -> str:
    if x is None:
        return ""
    return f"{x:.{nd}f}".rstrip("0").rstrip(".")


def safe_div(a: float, b: float) -> float | None:
    if b <= 0:
        return None
    return a / b


def score_efficiency(cpl: float | None, baseline: float | None) -> str:
    if cpl is None or baseline is None or baseline <= 0:
        return ""
    # lower CPL is better -> score up when cpl below baseline
    ratio = baseline / cpl if cpl > 0 else 0.0
    s = min(100.0, max(0.0, ratio * 50))
    return fmt_float(s, 1)


def build_kpi_rows(weeks: list[dict]) -> list[dict]:
    rows = []
    for w in weeks:
        spend = w["total_spend"]
        leads = w["total_leads"]
        won = w["ganado"]
        cpl = safe_div(spend, float(leads))
        cac = safe_div(spend, float(won)) if won > 0 else None
        l2s = safe_div(float(won), float(leads)) if leads > 0 else None
        rows.append(
            {
                "week_start": w["week_start"],
                "week_end": w["week_end"],
                "total_paid_spend": fmt_float(spend, 2),
                "total_leads": str(leads),
                "new_customers": str(won),
                "attributed_revenue": "",
                "cpl": fmt_float(cpl, 2) if cpl is not None else "",
                "cac": fmt_float(cac, 2) if cac is not None else "",
                "lead_to_sale_rate": fmt_float(l2s, 6) if l2s is not None else "",
                "roas": "",
                "closing_velocity_days": "",
                "notes": f"Cohort {w['label'][:12]}… HubSpot CRM + weekly paid spend",
            }
        )
    return rows


def build_channel_rows(
    weeks: list[dict],
    organic_counts: dict[tuple[str, str], int],
    recent_cpl_baseline: float | None,
) -> list[dict]:
    out = []
    for w in weeks:
        ws, we = w["week_start"], w["week_end"]
        key = (ws, we)
        organic_leads = organic_counts.get(key, 0)
        spend_total = w["meta_spend"] + w["google_spend"]
        paid_leads = max(0, w["total_leads"] - organic_leads)
        m_s, g_s = w["meta_spend"], w["google_spend"]
        if spend_total > 0:
            m_share = m_s / spend_total
            g_share = g_s / spend_total
        else:
            m_share = g_share = 0.5
        m_leads = int(round(paid_leads * m_share))
        g_leads = max(0, paid_leads - m_leads)
        won = w["ganado"]
        m_won = int(round(won * m_share)) if spend_total > 0 else (won // 2)
        g_won = max(0, won - m_won)

        for channel, sp, ld, nw in (
            ("meta", m_s, m_leads, m_won),
            ("google", g_s, g_leads, g_won),
            ("organic", 0.0, organic_leads, 0),
        ):
            if channel == "organic":
                cpl = None
            elif sp > 0 and ld > 0:
                cpl = safe_div(sp, float(ld))
            else:
                cpl = None
            cac = safe_div(sp, float(nw)) if sp > 0 and nw > 0 else None
            l2s = safe_div(float(nw), float(ld)) if ld > 0 else None
            eff = score_efficiency(cpl, recent_cpl_baseline)
            qual = fmt_float(min(100.0, (nw / ld * 500)) if ld > 0 else 0, 1) if ld > 0 else ""
            scale = fmt_float(min(100.0, ld / 3.0), 1) if ld > 0 else ""
            total_sc = ""
            if eff and qual and scale:
                try:
                    total_sc = fmt_float((float(eff) * 0.4 + float(qual) * 0.35 + float(scale) * 0.25), 1)
                except ValueError:
                    total_sc = ""
            out.append(
                {
                    "week_start": ws,
                    "week_end": we,
                    "channel": channel,
                    "spend": fmt_float(sp, 2),
                    "leads": str(ld),
                    "qualified_leads": str(w["qualified_proxy"]) if channel == "meta" else "",
                    "new_customers": str(nw),
                    "attributed_revenue": "",
                    "cpl": fmt_float(cpl, 2) if cpl is not None else "",
                    "cac": fmt_float(cac, 2) if cac is not None else "",
                    "lead_to_sale_rate": fmt_float(l2s, 6) if l2s is not None else "",
                    "roas": "",
                    "efficiency_score": eff,
                    "quality_score": qual,
                    "scale_score": scale,
                    "total_score": total_sc,
                    "notes": "Spend-split proxy for paid; organic from HubSpot fuente"
                    if channel != "organic"
                    else "Organic = redes + búsqueda orgánica",
                }
            )
    return out


def build_recommendations(last_week: dict, channel_last: dict[str, dict]) -> list[dict]:
    """Simple rules from latest week channel metrics."""
    recs = []
    meta = channel_last.get("meta", {})
    google = channel_last.get("google", {})
    org = channel_last.get("organic", {})

    def one(ch: str, d: dict):
        cpl_s = d.get("cpl") or ""
        try:
            cpl = float(cpl_s) if cpl_s else None
        except ValueError:
            cpl = None
        leads = int(d.get("leads") or 0)
        if ch == "meta":
            if cpl and cpl > 350:
                return ("decrease_budget", "CPL above 350 MXN vs recent cohort average", "-5%", "Watch CPL")
            if leads >= 100:
                return ("keep_budget", "Volume healthy; tune creatives", "0%", " steady")
            return ("increase_budget", "Scale test if CPL acceptable", "10%", "More leads")
        if ch == "google":
            if cpl and cpl > 25 and leads < 5:
                return ("increase_budget", "Low volume on Google; expand keywords/geo", "15%", "More leads")
            return ("keep_budget", "Monitor search intent quality", "0%", " steady")
        # organic
        if leads >= 10:
            return ("keep_budget", "Strong organic assist; keep content cadence", "0%", "Brand")
        return ("keep_budget", "Grow organic pipeline", "0%", "Content")

    for ch in ("meta", "google", "organic"):
        d = channel_last.get(ch, {})
        rec, reason, imp, sales = one(ch, d)
        recs.append(
            {
                "week_start": last_week["week_start"],
                "week_end": last_week["week_end"],
                "channel": ch,
                "current_budget": d.get("spend", "0"),
                "recommended_budget_change_percent": imp.replace("%", "").strip() if "%" in imp else "0",
                "recommendation": rec,
                "primary_reason": reason,
                "expected_leads_impact": imp,
                "expected_sales_impact": sales,
                "confidence": "medium",
                "owner": "marketing_lead",
                "next_review_date": "",
            }
        )
    return recs


def main() -> None:
    INSIGHTS.mkdir(parents=True, exist_ok=True)
    DOCS_INSIGHTS.mkdir(parents=True, exist_ok=True)

    weeks = load_cohort_weeks()
    if not weeks:
        raise SystemExit(f"No cohort rows found in {COHORT_FILE}")

    organic_counts = load_organic_counts_by_week(weeks)
    recent = weeks[-8:] if len(weeks) >= 8 else weeks
    recent_cpl_vals = []
    for w in recent:
        s, l = w["total_spend"], w["total_leads"]
        if l > 0:
            recent_cpl_vals.append(s / l)
    baseline_cpl = sum(recent_cpl_vals) / len(recent_cpl_vals) if recent_cpl_vals else None

    kpi_fields = [
        "week_start",
        "week_end",
        "total_paid_spend",
        "total_leads",
        "new_customers",
        "attributed_revenue",
        "cpl",
        "cac",
        "lead_to_sale_rate",
        "roas",
        "closing_velocity_days",
        "notes",
    ]
    kpi_rows = build_kpi_rows(weeks)

    ch_fields = [
        "week_start",
        "week_end",
        "channel",
        "spend",
        "leads",
        "qualified_leads",
        "new_customers",
        "attributed_revenue",
        "cpl",
        "cac",
        "lead_to_sale_rate",
        "roas",
        "efficiency_score",
        "quality_score",
        "scale_score",
        "total_score",
        "notes",
    ]
    channel_rows = build_channel_rows(weeks, organic_counts, baseline_cpl)

    last = weeks[-1]
    # channel rows for last week only for recommendations — extract three channels
    ch_last: dict[str, dict] = {}
    for r in channel_rows:
        if r["week_start"] == last["week_start"] and r["week_end"] == last["week_end"]:
            ch_last[r["channel"]] = r
    rec_rows = build_recommendations(last, ch_last)

    rec_fields = [
        "week_start",
        "week_end",
        "channel",
        "current_budget",
        "recommended_budget_change_percent",
        "recommendation",
        "primary_reason",
        "expected_leads_impact",
        "expected_sales_impact",
        "confidence",
        "owner",
        "next_review_date",
    ]

    def write_csv(path: Path, fields: list[str], rows: list[dict]) -> None:
        with path.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            for row in rows:
                w.writerow({k: row.get(k, "") for k in fields})

    write_csv(INSIGHTS / "weekly_kpi_dashboard.csv", kpi_fields, kpi_rows)
    write_csv(INSIGHTS / "weekly_channel_dashboard.csv", ch_fields, channel_rows)
    write_csv(INSIGHTS / "weekly_channel_budget_recommendations.csv", rec_fields, rec_rows)

    for name in (
        "weekly_kpi_dashboard.csv",
        "weekly_channel_dashboard.csv",
        "weekly_channel_budget_recommendations.csv",
    ):
        shutil.copy2(INSIGHTS / name, DOCS_INSIGHTS / name)

    print(f"Wrote {len(kpi_rows)} KPI weeks, {len(channel_rows)} channel rows, {len(rec_rows)} recs.")
    print(f"Latest week: {last['week_start']} .. {last['week_end']} | leads={last['total_leads']} spend={last['total_spend']:.0f} MXN ganado={last['ganado']}")


if __name__ == "__main__":
    main()
