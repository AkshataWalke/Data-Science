create table account(
	user_id serial primary key,
	username varchar(50) unique not null,
	password varchar(50) not null,
	email varchar(250) unique not null,
	created_on timestamp not null,
	last_login timestamp
)

create table job(
	job_id serial primary key,
	jon_name varchar(300) unique not null
)
	
create table account_job1(
	user_id integer references account(user_id),
	job_id integer references job(job_id),
	hire_date timestamp
)

select * from account
insert into account(username,password,email,created_on)
values 
('jose','password','jose@email.com',current_timestamp)

select * from account

insert into job(jon_name)
values('Astronaut')

select *from job
insert into job (jon_name)values('President')
 
insert into account_job1(user_id,job_id,hire_date)
values (1,1,current_timestamp)
select *from account_job1

insert into account_job1(user_id,job_id,hire_date)
values (10,10,current_timestamp)----foreign key constaints error

insert into account(username,password,email,created_on)values('Ram','root','ram1@sanjivani.org.in',current_timestamp)
select *from account
	
insert into job(jon_name)values('Data_scientist')

update account set last_login=current_timestamp where last_login is null;
select *from account

update account set last_login=created_on
select *from account
	
select *from account_job1
update account_job1
set hire_date=account.created_on
from account
where account_job1.user_id=account.user_id	
select *from account_job1



	
select *from job