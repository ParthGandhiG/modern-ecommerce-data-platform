-- Warehouse-facing model; adapt database/schema names to your account.
create or replace view analytics.v_customer_revenue as
select customer_id, sum(revenue) as revenue, count(distinct order_id) as orders,
       sum(revenue) / nullif(count(distinct order_id),0) as aov
from analytics.fct_orders
where status = 'completed'
group by customer_id;
