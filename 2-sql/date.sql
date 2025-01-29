show timezone

create table timezones(
	ts TIMESTAMP WITHOUT TIME ZONE,
	t2 TIMESTAMP WITH TIME ZONE
)

select *from timezones

insert into timezones VALUES(
	TIMESTAMP WITHOUT TIME ZONE '2023-03-07 10:50',
	TIMESTAMP WITH TIME ZONE '2023-03-07 10:50'
)

select now()::date;
select current_date

select to_char(current_date,'dd/mm/yy')

select to_char(current_date,'DDD')

select to_char(current_date,'WW')

select age(date'1800-01-01')

select age(date '1992/11/13',date'1800/01/01')

select extract(day from date'1992/11/13')AS DAY

select extract(month from date'1992/11/13')AS month

select extract(year from date'1992/11/13')AS year

select date_trunc('year',date'1992/11/13')

select age(birth_date),*from employees
where(
	extract(year from age(birth_date))
)>60;

select count(birth_date) from employees
where birth_date<now()-interval'61 years'

select count(emp_no)from employees
where extract(month from hire_date)=2;

select count(emp_no)from employees
where extract (MONTH from birth_date)=11

select max (birth_date) from employees
	
select max(salary)from salaries

select *,
max(salary)over()
from salaries

select *,
max(salary)over()
from salaries
limit 100

select *,
max(salary)over()
from salaries
where salary<70000

select *,
AVG(salary)OVER()
from salaries

select *,
	d.dept_name,
AVG(salary)OVER()
from salaries
JOIN dept_emp AS de USING(emp_no)
JOIN departments AS d using(dept_no)

select *,
	d.dept_name,
AVG(salary)OVER(PARTITION BY d.dept_name)
from salaries
JOIN dept_emp AS de USING(emp_no)
JOIN departments AS d using(dept_no)

select *,
AVG(salary)OVER(PARTITION BY d.dept_name)
from salaries
JOIN dept_emp AS de USING(emp_no)
JOIN departments AS d using(dept_no)


