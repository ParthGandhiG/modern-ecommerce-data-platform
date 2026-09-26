select customer_id, customer_name, city, email from {{ source('raw','customers') }}
