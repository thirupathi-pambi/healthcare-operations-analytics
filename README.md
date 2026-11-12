
# Clinic Operations KPI Report

This is a weekly-ops style report for a pretend network of three clinics. I wanted to start from raw appointment records and get to the numbers a clinic manager looks at every week: how many patients didn't show up, how many cancelled, and how each site compares. I built it twice, once in Python with an HTML dashboard and once in SQL, so I could check that both give the same answers.

All the appointment data is made up.

## The data

`data/appointments.csv` has 120 appointments across West, Central and North clinics, from January to June 2026, with 7 providers. Each row looks like this:

```
appointment_id,date,clinic,provider_id,status,scheduled_minutes
A0007,2026-02-08,West Clinic,PROV01,no_show,30
```

The `status` column is one of `completed`, `no_show` or `cancelled`.

## Running it

You need Python 3.10 or newer. There's nothing to install.

```bash
python src/main.py
python -m unittest discover -s tests
```

Run both commands from the repo root. This creates `output/dashboard.html`, which you can open in any browser. It shows KPI cards at the top and a table for each clinic below.

## Results

| Metric            | Value |
|-------------------|-------|
| Appointments      | 120   |
| Completed         | 84    |
| No-show rate      | 20.0% |
| Cancellation rate | 10.0% |

By clinic:

| Clinic  | Appts | Completed | No-show | Cancelled |
|---------|-------|-----------|---------|-----------|
| Central | 40    | 28        | 8       | 4         |
| North   | 40    | 28        | 8       | 4         |
| West    | 40    | 28        | 8       | 4         |

A 20% no-show rate is high. If this were real, it would be the first thing I'd raise, since each no-show is a slot that could have gone to another patient.

## SQL version

`sql/kpis.sql` produces the per-clinic numbers in plain SQL that works in SQLite and most BI tools. I loaded the CSV into SQLite and ran it to make sure the results matched the Python output, and they do for every clinic.

## Some decisions I made

- **Rates use all booked appointments as the denominator.** No-show % is no-shows divided by every appointment, including cancelled ones. Some organizations leave cancellations out of that denominator. I picked one definition and used the same one in both Python and SQL, so the two always agree.
- **The dashboard is one static HTML file.** It doesn't need a server, a login or any libraries. You can email it or open it from a shared drive.
- **An empty file doesn't crash.** With zero appointments, the rates come out as 0 instead of a divide-by-zero error. There's a test for this.

## Files

```
data/appointments.csv   fictional appointment records
src/main.py             KPI calculations and HTML dashboard
sql/kpis.sql            per-clinic KPIs in SQL
tests/test_main.py      unit tests for the rate math
output/dashboard.html   generated dashboard
```

## What I'd add next

- Schedule utilization. `scheduled_minutes` is already in the data, but I'd need clinic capacity (available minutes per day) to calculate it properly.
- Monthly trend lines, since the data covers six months
- A breakdown by provider. `provider_id` is in the data but isn't used yet.
- More varied sample data. Right now all three clinics come out identical, which isn't realistic and doesn't show off the comparison table.
