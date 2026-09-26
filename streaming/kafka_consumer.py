"""Reference Kafka consumer for clickstream events."""
import os
from confluent_kafka import Consumer
def main():
 c=Consumer({'bootstrap.servers':os.getenv('KAFKA_BOOTSTRAP_SERVERS','localhost:9092'),'group.id':'ecommerce-gold','auto.offset.reset':'earliest'}); c.subscribe(['ecommerce-events'])
 try:
  while True:
   m=c.poll(1)
   if m and not m.error(): print(m.value().decode())
 finally: c.close()
if __name__=='__main__': main()
