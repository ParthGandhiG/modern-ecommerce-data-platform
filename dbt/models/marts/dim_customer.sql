select customer_id, customer_name, city, email, true as is_current from {{ ref('stg_customers') }}
