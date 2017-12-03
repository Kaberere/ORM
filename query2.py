from peewee import *
from dvdrental import Staff, Payment, Rental

psql_db = PostgresqlDatabase(
    "dvdrental", host="localhost", user="kaberere", password="", port="5432")

queries = (Staff.select()
           .join(Payment)
           .join(Staff)
           .group_by(Staff.first_name)
           .execute()
           )

for que in queries:
    print(que.first_name, que.last_name)
