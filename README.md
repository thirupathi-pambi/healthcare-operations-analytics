# Healthcare Operations Analytics & KPI Report

> **Portfolio demonstration | Synthetic / fictional data only**

Reproducible appointment-operations metrics generated from synthetic clinic appointment data, with SQL examples and an HTML dashboard.

## What this demonstrates
- Calculate no-show and cancellation rates, clinic utilization and encounter volumes
- Generate a shareable HTML KPI summary
- Provide SQL queries for conventional BI use

## Quick start
```bash
python src/main.py
python -m unittest discover -s tests
```

Python 3.10+ is recommended. Core functionality uses the Python standard library; no API keys or patient records are required. Run commands from the repository root.

## Repository contents
- `data/appointments.csv`: fictional appointment records
- `src/main.py`: KPI calculations and HTML dashboard
- `sql/kpis.sql`: reporting queries
- `output/dashboard.html`: generated in quick start

## Relevant skills
Python, healthcare operations, KPI design, SQL, data visualization, HTML

## Data and privacy
All records, facilities, identifiers, events and organizations in this repository are fabricated for demonstrations. This is **not** a production clinical system and does not contain real protected health information (PHI). Do not upload real patient data or confidential employer files. Outputs do not substitute for clinical, privacy, security, or regulatory review.

## How to discuss in an interview
Explain the input, validations or transformations, measurable outputs, tests, and what you would change for a real deployment (authentication, audit logs, monitoring, regulatory review, and secure storage). Describe this as a **personal portfolio project**, not as an implementation at an employer.

## License
MIT — see [LICENSE](LICENSE).
