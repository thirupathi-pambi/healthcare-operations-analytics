import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from main import summarize
class MetricsTests(unittest.TestCase):
 def test_rates(self):
  x=summarize([{'status':'completed','clinic':'A'},{'status':'no_show','clinic':'A'}]);self.assertEqual(x['no_show_rate'],50)
 def test_empty(self):self.assertEqual(summarize([])['total'],0)
