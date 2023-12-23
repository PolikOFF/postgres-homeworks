-- SQL-команды для создания таблиц
create table employees
(
	employee_id int primary key,
	first_name varchar(50) NOT NULL,
	last_name varchar(50) NOT NULL,
	title varchar(50) NOT NULL,
	birth_date date NOT NULL,
	notes text NOT NULL
);

create table customers
(
	customer_id varchar(5) primary key NOT NULL,
	company_name varchar(50) NOT NULL,
	contact_name varchar(50) NOT NULL
);

create table orders
(
	order_id int primary key,
	customer_id varchar(5) references customers(customer_id) NOT NULL,
	employee_id int references employees(employee_id) NOT NULL,
	order_date date NOT NULL,
	ship_city varchar(50) NOT NULL
)