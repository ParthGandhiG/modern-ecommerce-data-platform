select order_id, customer_id, product_id, quantity, unit_price, status, cast(order_ts as timestamp) as order_ts
from {{ source('raw','orders') }}
