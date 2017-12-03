from peewee import *
from dvdrental import Customer, Payment, Rental, Inventory

psql_db = PostgresqlDatabase(
    "dvdrental", host="localhost", user="kaberere", password="27538204079", port="5432")

queries = (Customer.select(Customer.first_name, Customer.last_name, Payment.amount)
           .join(Rental)
           .join(Payment)
           .where(Payment.amount > 6)
           .order_by(Rental.rental.desc())
           .limit(10)
           .naive()
           )
for que in queries:
    print(que.first_name, que.last_name, que.amount)
