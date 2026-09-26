"""Reference Kafka producer. Install confluent-kafka and set KAFKA_BOOTSTRAP_SERVERS to run against Kafka."""
import json,os
from time import sleep
from random import randint,choice

def main():
 from confluent_kafka import Producer
 p=Producer({'bootstrap.servers':os.getenv('KAFKA_BOOTSTRAP_SERVERS','localhost:9092')})
 for i in range(10):
  event={'event_id':i,'customer_id':randint(1,100),'event_type':choice(['page_view','product_view','add_to_cart','purchase'])}
  p.produce('ecommerce-events',json.dumps(event).encode()); p.poll(0); sleep(.2)
 p.flush()
if __name__=='__main__': main()
