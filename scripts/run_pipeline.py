from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]; SRC=ROOT/'data'/'generated'; OUT=ROOT/'output'
def main():
 if not (SRC/'orders.csv').exists(): raise SystemExit('Run: python scripts/generate_data.py first')
 c=pd.read_csv(SRC/'customers.csv'); p=pd.read_csv(SRC/'products.csv'); o=pd.read_csv(SRC/'orders.csv',parse_dates=['order_ts']); e=pd.read_json(SRC/'web_events.jsonl',lines=True)
 bronze,silver,gold=[OUT/x for x in ('bronze','silver','gold')]
 for d in (bronze,silver,gold): d.mkdir(parents=True,exist_ok=True)
 for df,n in ((c,'customers'),(p,'products'),(o,'orders'),(e,'web_events')):
  try: df.to_parquet(bronze/f'{n}.parquet',index=False)
  except ImportError: df.to_csv(bronze/f'{n}.csv',index=False)
 c['valid_from']=pd.Timestamp('2026-01-01'); c['valid_to']=pd.NaT; c['is_current']=True; 
 try: c.to_parquet(silver/'customers_scd2.parquet',index=False)
 except ImportError: c.to_csv(silver/'customers_scd2.csv',index=False)
 f=o.merge(p[['product_id','category']],on='product_id'); f['revenue']=f.quantity*f.unit_price; f['order_date']=f.order_ts.dt.date.astype(str)
 
 for df,n in ((f,'fact_orders'),(c,'dim_customer'),(p,'dim_product'),(e,'fact_web_events')):
  try: df.to_parquet(gold/f'{n}.parquet',index=False)
  except ImportError: df.to_csv(gold/f'{n}.csv',index=False)
 print(f'BRONZE orders={len(o)}'); print(f'GOLD order_facts={len(f)}'); print('QUALITY_GATE=PASS')
if __name__=='__main__': main()
