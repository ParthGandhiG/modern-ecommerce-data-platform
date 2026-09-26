from pathlib import Path
import random,csv,json
from datetime import datetime,timedelta
random.seed(42)
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'data'/'generated'; OUT.mkdir(parents=True,exist_ok=True)
cities=['Chennai','Bengaluru','Mumbai','Delhi','Pune','Hyderabad']; cats=['Electronics','Home','Fashion','Sports','Books']
products=[(i,f'Product {i}',random.choice(cats),round(random.uniform(10,500),2)) for i in range(1,51)]
customers=[(i,f'Customer {i}',random.choice(cities),f'customer{i}@example.com') for i in range(1,101)]
for name,header,rows in [('customers.csv',['customer_id','customer_name','city','email'],customers),('products.csv',['product_id','product_name','category','unit_price'],products)]:
 with open(OUT/name,'w',newline='') as f: w=csv.writer(f); w.writerow(header); w.writerows(rows)
start=datetime(2026,1,1); orders=[]
for i in range(1,1001):
 p=random.choice(products); ts=start+timedelta(days=random.randint(0,180),minutes=random.randint(0,1439)); orders.append([i,random.randint(1,100),p[0],random.randint(1,5),p[3],random.choices(['completed','cancelled','returned'],[.82,.10,.08])[0],ts.isoformat()])
with open(OUT/'orders.csv','w',newline='') as f: w=csv.writer(f); w.writerow(['order_id','customer_id','product_id','quantity','unit_price','status','order_ts']); w.writerows(orders)
with open(OUT/'web_events.jsonl','w') as f:
 for i in range(1,5001):
  ts=start+timedelta(days=random.randint(0,180),minutes=random.randint(0,1439)); f.write(json.dumps({'event_id':i,'customer_id':random.randint(1,100),'event_type':random.choice(['page_view','product_view','add_to_cart','checkout','purchase']),'event_ts':ts.isoformat()})+'\n')
print(f'Generated synthetic data in {OUT}')
