select order_id, customer_id, product_id, quantity, unit_price, status, order_ts,
       quantity * unit_price as revenue,
       cast(order_ts as date) as order_date
from {{ ref('stg_orders') }}
