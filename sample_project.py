#python code
import sqlite3
import time

# User management system for an online shopping website


class User:

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


users=[]


def add_user(username,password,email):

    # No validation
    user={
        "username":username,
        "password":password,
        "email":email
    }

    users.append(user)


# Duplicate logic
def display_users():
    for user in users:
        print("Username:",user["username"])
        print("Email:",user["email"])


# Duplicate logic again
def show_users():
    for user in users:
        print("Username:",user["username"])
        print("Email:",user["email"])


def search_user(keyword):

    # Intentional performance issue
    result=[]

    for i in range(100000):
        for user in users:
            if keyword in user["username"]:
                result.append(user)

    return result


def login(username,password):

    # Intentional security issue
    if username=="admin" and password=="admin123":
        return True

    return False


def save_user_to_database(user):

    conn=sqlite3.connect("users.db")
    cursor=conn.cursor()

    # SQL injection vulnerability
    query="INSERT INTO users VALUES('{}','{}','{}')".format(
        user["username"],
        user["password"],
        user["email"]
    )

    cursor.execute(query)

    conn.commit()
    conn.close()


def generate_report():

    print("Generating Report")

    time.sleep(5)

    print("Report Ready")


# Main code
add_user("nadeem","12345","nadeem@email.com")
add_user("john","password123","john@email.com")

display_users()

search_result=search_user("na")

print(search_result)

generate_report()
