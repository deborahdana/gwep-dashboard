const DATA_PATHS = {
  weeklyKpi: "../GWEP/insights/weekly_kpi_dashboard.csv",
  channel: "../GWEP/insights/weekly_channel_dashboard.csv",
  recommendations: "../GWEP/insights/weekly_channel_budget_recommendations.csv",
};

function parseCsv(text) {
  const lines = text.trim().split(/\r?\n/);
  if (lines.length < 2) return [];
  const headers = lines[0].split(",").map((h) => h.trim());
  return lines.slice(1).map((line) => {
    const values = line.split(",");
    const row = {};
    headers.forEach((h, i) => {
      row[h] = (values[i] || "").trim();
    });
    return row;
  });
}

async function loadCsv(path) {
  const resp = await fetch(path);
  if (!resp.ok) throw new Error(`Could not load ${path}`);
  const text = await resp.text();
  return parseCsv(text);
}

function valueOrDash(v) {
  return v === "" || v == null ? "-" : v;
}

function formatPercent(v) {
  if (v === "" || v == null) return "-";
  const n = Number(v);
  if (Number.isNaN(n)) return v;
  return `${(n * 100).toFixed(1)}%`;
}

function renderTable(elId, rows) {
  const table = document.getElementById(elId);
  if (!rows.length) {
    table.innerHTML = "<tr><td>No data yet</td></tr>";
    return;
  }
  const headers = Object.keys(rows[0]);
  const thead = `<thead><tr>${headers.map((h) => `<th>${h}</th>`).join("")}</tr></thead>`;
  const tbody = rows
    .map((r) => `<tr>${headers.map((h) => `<td>${valueOrDash(r[h])}</td>`).join("")}</tr>`)
    .join("");
  table.innerHTML = `${thead}<tbody>${tbody}</tbody>`;
}

function latestWeek(rows) {
  if (!rows.length) return null;
  return rows[rows.length - 1];
}

function latestWeekRows(rows) {
  if (!rows.length) return [];
  const last = rows[rows.length - 1];
  return rows.filter((r) => r.week_start === last.week_start && r.week_end === last.week_end);
}

async function boot() {
  try {
    const [weeklyKpiRows, channelRows, recommendationRows] = await Promise.all([
      loadCsv(DATA_PATHS.weeklyKpi),
      loadCsv(DATA_PATHS.channel),
      loadCsv(DATA_PATHS.recommendations),
    ]);

    const latestKpi = latestWeek(weeklyKpiRows);
    if (latestKpi) {
      document.getElementById("kpi-cpl").textContent = valueOrDash(latestKpi.cpl);
      document.getElementById("kpi-cac").textContent = valueOrDash(latestKpi.cac);
      document.getElementById("kpi-lts").textContent = formatPercent(latestKpi.lead_to_sale_rate);
      document.getElementById("kpi-roas").textContent = valueOrDash(latestKpi.roas);
      document.getElementById("kpi-velocity").textContent = valueOrDash(latestKpi.closing_velocity_days);
      document.getElementById("latest-week-meta").textContent = `${latestKpi.week_start} to ${latestKpi.week_end}`;
      renderTable("weekly-kpi-table", [latestKpi]);
    } else {
      renderTable("weekly-kpi-table", []);
    }

    renderTable("channel-table", latestWeekRows(channelRows));
    renderTable("recommendation-table", latestWeekRows(recommendationRows));
  } catch (err) {
    document.body.innerHTML = `<main class="container"><p>Dashboard load error: ${err.message}</p></main>`;
  }
}

boot();
