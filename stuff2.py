from peewee import PostgresqlDatabase, Model, CharField, DateTimeField
import psycopg2
import psycopg2.extras
import datetime

psql_db = PostgresqlDatabase(
    "dvdrental", host="localhost", user="kaberere", password="27538204079", port="5432")


class RentMovie(Model):

    class Meta:
        database = psql_db

    renter_name = CharField(20)
    movie_name = CharField(20)
    rental_date = DateTimeField(default=datetime.datetime.now)
    return_date = DateTimeField(default=datetime.datetime.now)


if __name__ == '__main__':
    conn = psycopg2.connect(
        dbname="dvdrental", user="kaberere", host="localhost", password="27538204079")
    RentMovie.create_table(fail_silently=True)
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("""SELECT title AS movie_name, rental_date, last_name AS renter_name FROM rental\
        JOIN inventory ON (rental.inventory_id = inventory.inventory_id)\
        JOIN film ON (inventory.film_id = film.film_id)\
        JOIN customer ON (customer.customer_id = rental.customer_id)\
        WHERE rental_date IS NOT null\
        ORDER BY rental_date DESC LIMIT 10;""")
    results = cur.fetchall()

    for result in results:
        rentals = RentMovie(**result)
    rentals.save()
