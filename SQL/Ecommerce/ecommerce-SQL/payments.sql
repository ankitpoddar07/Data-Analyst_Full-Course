-- SELECT * FROM ecommerce.payments;

/* multiple conditions
select * from payments where payment_type = "UPI" and payment_value >= 500;  */

-- select * from payments where payment_value between 150 and 200;

-- select * from payments limit 2,4 ;

-- select sum(payment_value) as total_revenue from payments;
select round(sum(payment_value),2) as total_revenue from payments;
