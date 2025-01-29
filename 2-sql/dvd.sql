---select category_col,AGG(data_col) from table GROUP BY category_col
---select category_col,AGG(data_col) from table where category_col!='A' GROUP BY category_col
---select company,division,SUM(sales) from finance_table GROUP BY company 

---when you want to sort results based on the aggregate function
---select company,division,SUM(sales) from finance_table GROUP BY company ORDER BY SUM(sales)

select customer_id,staff_id,SUM(amount) from payment
GROUP BY staff_id,customer_id

select staff_id,customer_id,SUM(amount) from payment
GROUP BY staff_id,customer_id

select staff_id,customer_id,SUM(amount) from payment
GROUP BY staff_id,customer_id
Order by customer_id

select staff_id,customer_id,SUM(amount) from payment
GROUP BY staff_id,customer_id
Order by staff_id

select staff_id,customer_id,SUM(amount) from payment
GROUP BY staff_id,customer_id
Order by staff_id,customer_id

select staff_id,customer_id,SUM(amount) from payment
GROUP BY staff_id,customer_id
Order by SUM(amount)

select * from payment

select DATE(payment_date) from payment

select DATE(payment_date),SUM(amount) from payment
GROUP BY DATE(payment_date)

select DATE(payment_date),SUM(amount) from payment
GROUP BY DATE(payment_date)
ORDER BY sum(amount)

select DATE(payment_date),SUM(amount) from payment
GROUP BY DATE(payment_date)
ORDER BY sum(amount) DESC

---we have two staff members,with staff IDs 1 and 2.we want to give a bonus to the staff member tht handled the most payments.
---how many payments did each staff member handle and who gets the bonus
select staff_id,count(amount)
from payment
Group by staff_id

---corporate HQ is conducting a study on the relationship bet replacement cost and a movie MPAA rating
---what is the average replacement cost per MPAA rating

select rating,AVG(replacement_cost) from film GROUP BY rating

select rating,Round(AVG(replacement_cost)2)
from film group by rating

---we are running a promotion to reward our top 5 customers with coupons
---what are the customer ids of the top 5 customers by total spend
select customer_id,sum(amount)from payment
group by customer_id
order by sum(amount) desc limit 5 

select customer_id from payment
group by customer_id

select customer_id,sum(amount) from payment
group by customer_id

-------------------having clause---------------------
select company,sum(sales)
from finance_table
where company!='Google'
group by company

select customer_id,sum(amount) from payment
where customer_id not in(148,57) 
group by customer_id

select customer_id,sum(amount) from payment
group by customer_id
having sum(amount)>100
