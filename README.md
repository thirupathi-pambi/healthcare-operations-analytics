# Healthcare Operations Analytics & KPI Report

![Python](https://img.shields.io/badge/python-3.10%2B-blue) ![License](https://img.shields.io/badge/license-MIT-green)

Reproducible appointment-operations metrics for a clinic network, delivered three ways: a Python script, a static HTML dashboard, and equivalent SQL queries for BI tools.

> Built on synthetic appointment data only. No real patient information is included.

## Why this exists

Clinic operations teams track a handful of numbers every week: how many patients don't show, how many cancel, and how well schedules are used. This project computes those KPIs from raw appointment records and presents them in a form both analysts (SQL) and managers (HTML) can use.

## KPIs

- No-show rate
- Cancellation rate
- Clinic utilization
- Encounter volumes

## Project structure

```
.
├── data/
│   └── appointments.csv       # fictional appointment records
├── src/
│   └── main.py                # KPI calculations and HTML dashboard generation
├── sql/
│   └── kpis.sql               # the same KPIs as reporting queries
├── tests/
│   └── test_main.py
├── output/
│   └── dashboard.html         # generated report (open in any browser)
├── LICENSE
└── README.md
```

## Quick start

Requires Python 3.10+ (standard library only). Run from the repository root.

```bash
python src/main.py                      # regenerates output/dashboard.html
python -m unittest discover -s tests
```

Then open `output/dashboard.html` in a browser.

## Limitations and next steps

- Static snapshot; no filtering by date range or clinic in the browser.
- Utilization depends on how capacity is defined in the sample data; real definitions vary by organization.
- Possible extensions: trend lines over time, per-provider breakdowns, and loading the data into a database so the SQL queries run against it directly.

## License

MIT. See [LICENSE](LICENSE).
