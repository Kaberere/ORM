from peewee import PostgresqlDatabase, Model, CharField, DateTimeField
from dvdrental import Rental, Customer, Inventory, Film, Rentmovie

psql_db = PostgresqlDatabase(
    "dvdrental", host="localhost", user="kaberere", password="27538204079", port="5432")

if __name__ == '__main__':
    query = (Rental.select()
             .order_by(Rentmovie.rental_date.desc())
             .limit(10)
             .naive()
             )
for que in query:
    print(que.Customer.last_name)
