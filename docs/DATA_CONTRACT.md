# Data Contract: Orders

**Owner:** Commerce Data Platform

**Business key:** `order_id`

**Required fields:** order_id, customer_id, product_id, quantity, unit_price, status, order_ts

**Allowed status:** completed, cancelled, returned

**Compatibility:** additive fields are backward compatible; renames/removals require a version bump and downstream impact assessment.

**Quality gates:** uniqueness, nullability, foreign-key integrity, positive quantity, accepted status, timestamp parseability.
