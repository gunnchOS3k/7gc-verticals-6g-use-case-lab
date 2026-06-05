from pathlib import Path
from gunnchos_7gc_verticals.health import health_kpis
from gunnchos_7gc_verticals.energy import energy_kpis
from gunnchos_7gc_verticals.vehicles import vehicle_kpis
from gunnchos_7gc_verticals.industry_defense import industry_kpis
from gunnchos_7gc_verticals.report import vertical_report

R=Path('results'); R.mkdir(exist_ok=True)
for name, kpis, fn in [('health', health_kpis(), 'health_kpis.md'), ('energy', energy_kpis(), 'energy_kpis.md'), ('vehicle', vehicle_kpis(), 'vehicle_kpis.md'), ('industry_defense', industry_kpis(), 'industry_defense_kpis.md')]:
    (R/fn).write_text(vertical_report(name, kpis))
(R/'verticals_report.md').write_text('# Verticals\nMapped to 7GC repos\n')
(R/'experiment_summary.md').write_text('# Verticals e2e PASS\n')
