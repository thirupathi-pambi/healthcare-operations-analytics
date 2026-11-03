import csv
from collections import Counter, defaultdict
from pathlib import Path
from html import escape
ROOT = Path(__file__).resolve().parents[1]

def summarize(rows):
    rows = list(rows)
    totals = Counter(r['status'] for r in rows)
    clinics = defaultdict(Counter)
    for r in rows: clinics[r['clinic']][r['status']] += 1
    n = len(rows)
    return {'total': n, 'completed': totals['completed'], 'no_show_rate': round(100*totals['no_show']/n,1) if n else 0,
            'cancellation_rate': round(100*totals['cancelled']/n,1) if n else 0,
            'clinics': {k:dict(v) for k,v in sorted(clinics.items())}}

def main():
    with (ROOT/'data/appointments.csv').open(newline='') as f: stats=summarize(csv.DictReader(f))
    cards = ''.join(f'<div class="card"><b>{escape(k.replace("_", " ").title())}</b><h2>{v}{"%" if "rate" in k else ""}</h2></div>'
                    for k,v in stats.items() if k!='clinics')
    table = ''.join(f'<tr><td>{escape(name)}</td><td>{sum(s.values())}</td><td>{s.get("completed",0)}</td><td>{s.get("no_show",0)}</td><td>{s.get("cancelled",0)}</td></tr>' for name,s in stats['clinics'].items())
    html = f"""<!doctype html><html lang="en"><meta charset="utf-8"><title>Clinic KPI Dashboard</title><style>body{{font:16px system-ui;margin:40px;background:#f4f7fb;color:#14283b}}.cards{{display:flex;flex-wrap:wrap;gap:16px}}.card{{background:white;border-radius:12px;padding:20px;min-width:150px;box-shadow:0 2px 7px #ddd}}table{{border-collapse:collapse;background:white;width:100%;margin-top:20px}}th,td{{padding:12px;text-align:left;border-bottom:1px solid #ddd}}</style><h1>Fictional Clinic Operations</h1><p>Portfolio simulation · synthetic appointment data</p><div class="cards">{cards}</div><h2>Site performance</h2><table><tr><th>Clinic</th><th>Visits</th><th>Completed</th><th>No-show</th><th>Cancelled</th></tr>{table}</table></html>"""
    out=ROOT/'output/dashboard.html';out.parent.mkdir(exist_ok=True);out.write_text(html)
    print(f'Created {out}')
if __name__=='__main__':main()
