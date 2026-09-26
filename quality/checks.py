from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]; SRC=ROOT/'data'/'generated'
def run_checks():
 c=pd.read_csv(SRC/'customers.csv'); p=pd.read_csv(SRC/'products.csv'); o=pd.read_csv(SRC/'orders.csv')
 checks={
 'customer_id_unique': c.customer_id.is_unique,
 'product_id_unique': p.product_id.is_unique,
 'order_id_unique': o.order_id.is_unique,
 'orders_customer_fk': o.customer_id.isin(c.customer_id).all(),
 'orders_product_fk': o.product_id.isin(p.product_id).all(),
 'positive_quantity': (o.quantity>0).all(),
 'valid_status': o.status.isin(['completed','cancelled','returned']).all(),
 }
 return checks
if __name__=='__main__':
 r=run_checks(); [print(f'{k}: {"PASS" if v else "FAIL"}') for k,v in r.items()]; raise SystemExit(0 if all(r.values()) else 1)
