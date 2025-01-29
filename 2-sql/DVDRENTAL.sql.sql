SELECT * FROM customer 
WHERE first_name LIKE 'A%'
ORDER BY last_name


SELECT * FROM customer 
WHERE first_name LIKE 'A%' AND last_name NOT LIKE 'B%'
ORDER BY last_name

SELECT COUNT(amount)FROM payment
WHERE amount>5;

select count(*) from actor
where first_name LIKE 'P%'

--how many unique Districts are our customers from
select count(distinct(district))
from address

--Retrive the list of names for those distinct districts from the previous question
select distinct(district)from address;

--how many films have a rating of R and a replacement cost between $5 and $15
select count(*)from film
where rating='R'
AND replacement_cost BETWEEN 5 AND 15;

--how many films have the word Truman somewhere in the title
select count(*)from film
Where title LIKE '%Truman%';


----------------AGGREGATE FUNCTIONS-------------------------------------------------


--Aggregate functions only in select and having clause

Select min(replacement_cost)from film;

Select max(replacement_cost)from film;

Select max(replacement_cost),min(replacement_cost)from film;

--Gruop by allows us to aggregate columns some category
--categorical columns are non-continuous

