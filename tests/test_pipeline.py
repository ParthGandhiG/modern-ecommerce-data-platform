import subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def test_generate_and_quality():
 subprocess.run([sys.executable,str(ROOT/'scripts/generate_data.py')],check=True)
 r=subprocess.run([sys.executable,str(ROOT/'quality/checks.py')],capture_output=True,text=True); assert r.returncode==0; assert 'FAIL' not in r.stdout
def test_pipeline():
 subprocess.run([sys.executable,str(ROOT/'scripts/run_pipeline.py')],check=True)
 assert (ROOT/'output'/'gold'/'fact_orders.parquet').exists() or (ROOT/'output'/'gold'/'fact_orders.csv').exists()
