import sqlite3

def print_result(result, message):
    print(message)
    for row in result:
        print(row)

def add_publisher(cursor, publisher_name):
    try:
        cursor.execute("INSERT INTO Publishers (publisher_name) VALUES (?)", (publisher_name,))
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        print(f"{publisher_name} is already in the database.")
        cursor.execute("SELECT publisher_id FROM Publishers WHERE publisher_name = ?", (publisher_name,))
        return cursor.fetchone()[0]

def add_magazine(cursor, magazine_name, publisher_id):
    try:
        cursor.execute("INSERT INTO Magazines (magazine_name, publisher_id) VALUES (?,?)", (magazine_name, publisher_id))
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        print(f"{magazine_name} is already in the database.")
        cursor.execute("SELECT magazine_id FROM Magazines WHERE magazine_name = ?", (magazine_name,))
        return cursor.fetchone()[0]

def add_subscriber(cursor, subscriber_name, subscriber_address):
    try:
        cursor.execute("""
            INSERT INTO Subscribers (subscriber_name, subscriber_address)
            VALUES (?,?)
        """, (subscriber_name, subscriber_address))
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        print(f"Subscriber '{subscriber_name}' at '{subscriber_address}' is already in the database.")
        cursor.execute("""
            SELECT subscriber_id FROM Subscribers
            WHERE subscriber_name = ? AND subscriber_address = ?
        """, (subscriber_name, subscriber_address))
        return cursor.fetchone()[0]

def add_subscription(cursor, subscriber_id, magazine_id, expiration_date):
    try:
        cursor.execute("""
            INSERT INTO Subscriptions (subscriber_id, magazine_id, expiration_date)
            VALUES (?,?,?)
        """, (subscriber_id, magazine_id, expiration_date))
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        print(f"Subscription for subscriber {subscriber_id} to magazine {magazine_id} already exists.")
        return None

# Task 1: Create a New SQLite Database
with sqlite3.connect("../db/magazines.db") as conn:
    try:
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        # Task 2: Define Database Structure
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Publishers (
            publisher_id INTEGER PRIMARY KEY,
            publisher_name TEXT NOT NULL UNIQUE
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Magazines (
            magazine_id INTEGER PRIMARY KEY,
            magazine_name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES Publishers (publisher_id)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            subscriber_name TEXT NOT NULL,
            subscriber_address TEXT NOT NULL,
            UNIQUE (subscriber_name, subscriber_address)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES Subscribers (subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES Magazines (magazine_id),
            UNIQUE (subscriber_id, magazine_id)
        )
        """)
        
        # Task 3: Populate Tables with Data
        print("Task 3: Populate Tables with Data")

        print("Inserting data into publishers")
        publisher_list = []
        for name in ['Time Life', 'The New York Times Company', 'Global Publishing']:
            publisher_list.append(add_publisher(cursor, name))

        print("Inserting data into magazines")
        magazine_list = []
        for name, pub_id in [('Readers Digest', publisher_list[0]),
                             ('New York Times', publisher_list[1]),
                             ('Global News', publisher_list[2])]:
            magazine_list.append(add_magazine(cursor, name, pub_id))

        print("Inserting data into subscribers")
        subscriber_list = []
        for name, address in [('Alice Dawson', '321 Pine St'),
                              ('William Phelps', '567 Oak Drive'),
                              ('Thomas Watson', '234 Flamingo Ave')]:
            subscriber_list.append(add_subscriber(cursor, name, address))

        print("Inserting data into subscriptions")
        subscription_list = []
        for i in range(3):
            subscription_list.append(
                add_subscription(cursor, subscriber_list[i], magazine_list[i], "2025-12-31")
            )

        conn.commit()
        print("Tables created and populated successfully.")
        
        print_result(cursor.execute("SELECT * FROM Publishers").fetchall(), "Publishers Table:")
        print_result(cursor.execute("SELECT * FROM Magazines").fetchall(), "Magazines Table:")
        print_result(cursor.execute("SELECT * FROM Subscribers").fetchall(), "Subscribers Table:")
        print_result(cursor.execute("SELECT * FROM Subscriptions").fetchall(), "Subscriptions Table:")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
