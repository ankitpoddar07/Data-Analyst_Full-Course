-- select * from ecommerce.customers;

/* select COLUMN NAME from TABLE NAME 
select customer_id, customer_city, customer_state from customers; */

-- select * from customers where customer_state = "SP" ;

-- select * from customers where customer_city like "%de%";

-- select count(customer_id) from customers;
select count(distinct customer_city) from customers;