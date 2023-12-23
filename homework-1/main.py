"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv


def get_data_from_csv(filename):
    with open(filename, 'r', newline='') as f:
        all_data = []
        full_data = csv.DictReader(f)
        for data in full_data:
            all_data.append(data)
        return all_data


customers = get_data_from_csv('north_data/customers_data.csv')
employees = get_data_from_csv('north_data/employees_data.csv')
orders = get_data_from_csv('north_data/orders_data.csv')

try:
    with psycopg2.connect(
        host='localhost',
        database='north',
        user='postgres',
        password='4505'
    ) as conn:
        with conn.cursor() as cur:
            for customer in range(len(customers)):
                cur.execute('INSERT INTO customers VALUES (%s, %s, %s)',
                            (customers[customer]['customer_id'],
                             customers[customer]['company_name'],
                             customers[customer]['contact_name']))

            for employee in range(len(employees)):
                cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)',
                            (employees[employee]['employee_id'],
                             employees[employee]['first_name'],
                             employees[employee]['last_name'],
                             employees[employee]['title'],
                             employees[employee]['birth_date'],
                             employees[employee]['notes']))

            for order in range(len(orders)):
                cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)',
                            (orders[order]['order_id'],
                             orders[order]['customer_id'],
                             orders[order]['employee_id'],
                             orders[order]['order_date'],
                             orders[order]['ship_city']))
finally:
    conn.close()
