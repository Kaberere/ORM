import psycopg2
import psycopg2.extras
import datetime

from dvdrental import Rentmovie


class Rental:

    def __init__(self, title, date_rented, customer):
        self.title = title
        self.date_rented = date_rented
        self.customer = customer

    def __repr__(self):
        return """\nFirst Name: {}\n
                   \nRental Date: {}\n
                   \nCustomer: {}\n
               """.format(self.title, self.date_rented, self.customer)

if __name__ == '__main__':
    conn = psycopg2.connect(
        dbname="dvdrental", user="kaberere", host="localhost", password="27538204079")
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("""SELECT title, rental_date AS date_rented, last_name AS customer FROM rental\
        JOIN inventory ON (rental.inventory_id = inventory.inventory_id)\
        JOIN film ON (inventory.film_id = film.film_id)\
        JOIN customer ON (customer.customer_id = rental.customer_id)\
        WHERE rental_date IS NOT null\
        ORDER BY rental_date DESC LIMIT 10;""")
    results = cur.fetchall()
    rentals = [Rental(**result) for result in results]
    print(rentals)
