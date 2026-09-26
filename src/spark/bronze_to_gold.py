"""PySpark/Delta reference pipeline for Azure Databricks.
Run in a Databricks cluster with delta-spark available.
"""
from pyspark.sql import SparkSession, functions as F

def build(input_path: str, output_path: str):
    spark = SparkSession.builder.appName('ecommerce-medallion').getOrCreate()
    orders = spark.read.option('header', True).csv(f'{input_path}/orders.csv')
    products = spark.read.option('header', True).csv(f'{input_path}/products.csv')
    customers = spark.read.option('header', True).csv(f'{input_path}/customers.csv')
    orders = (orders.withColumn('order_id',F.col('order_id').cast('long'))
                    .withColumn('customer_id',F.col('customer_id').cast('long'))
                    .withColumn('product_id',F.col('product_id').cast('long'))
                    .withColumn('quantity',F.col('quantity').cast('int'))
                    .withColumn('unit_price',F.col('unit_price').cast('double'))
                    .withColumn('order_ts',F.to_timestamp('order_ts'))
                    .dropDuplicates(['order_id']))
    silver = orders.join(products.select('product_id','category'), 'product_id', 'left')
    gold = silver.withColumn('revenue',F.col('quantity')*F.col('unit_price')).withColumn('order_date',F.to_date('order_ts'))
    gold.write.format('delta').mode('overwrite').partitionBy('order_date').save(f'{output_path}/fact_orders')
    customers.write.format('delta').mode('overwrite').save(f'{output_path}/dim_customer')
    spark.stop()
