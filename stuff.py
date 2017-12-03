from peewee import PostgresqlDatabase, Model, CharField, BooleanField, IntegerField

psql_db = PostgresqlDatabase(
    "ubuntu", host="localhost", user="postgres", password="secret", port="5432")

# My_User inherits all of the functionality from Model


class MyUser(Model):

    class Meta:
        # Tells Model to use psql_db connection
        database = psql_db

    age = IntegerField(4)  # An int field of size 4
    username = CharField(20)  # A username with length of 20
    password = CharField(10)
    email = CharField(30)

    is_beautiful = BooleanField(default=False)

if __name__ == "__main__":
    MyUser.create_table(fail_silently=True)

    new_user = MyUser(age="21", username="KaberereEve", password="secret",
                      email="kaberereeve44@gmail.com")

    new_user = MyUser(age="25", username="andiza",
                      password="O", email="koenaconcepts@gmail.com")
    new_user = MyUser(age="14", username="egikuri",
                      password="malenge", email="elvisgiks@gmail.com")
    new_user = MyUser(age="13", username="aberkowitz",
                      password="secret", email="aberkowitz@gmail.com")
    new_user.save()


for my_user in MyUser.select():
    print("email {0} at {1}".format(my_user.username, my_user.email))


is_KaberereEve = MyUser.select().where(
    MyUser.username == "KaberereEve").execute()
is_not_KaberereEve = MyUser.select().where(MyUser.username != "KaberereEve")
not_a_child = MyUser.select().where(MyUser.age > 21)
really_not_a_child = MyUser.select().where(
    (MyUser.age > 21)) & (MyUser.username != "kelvinty")
MyUser.delete().where(MyUser.age < 21).execute()
