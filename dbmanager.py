import sqlite3
import hashlib
import argparse
import random


conn = None
cursor = None


def open_and_create():
    global conn
    global cursor
    conn = sqlite3.connect('sql.db')
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM user")
    except sqlite3.OperationalError:
        # Create table
        cursor.execute('''CREATE TABLE user
                     (username TEXT, password TEXT, salt TEXT,
                      PRIMARY KEY (username))''')


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', help="add a username (requires -p)",
                        required=False)
    parser.add_argument('-p', help="the username password",
                        required=True)
    parser.add_argument('-c', help="check for a usernamename and password"
                                   "(requires -p)", required=False)
    return parser.parse_args()


def save_new_username_correct(username, password):
    global conn
    global cursor
    salt = str(random.random())
    concat = salt + password
    for i in range(1000):
        digest = hashlib.sha256(concat.encode('utf-8')).hexdigest()
    cursor.execute("INSERT OR REPLACE INTO user VALUES (?,?,?)",
                   (username, digest, salt))
    conn.commit()


def check_for_username_correct(username, password):
    global conn
    global cursor
    conn = sqlite3.connect('sql.db')
    cursor = conn.cursor()
    row = cursor.execute("SELECT * FROM user WHERE username = ?", (username,))
    results = row.fetchall()
    if results:
        salt = str(results[0][2])
        concat = salt + password
        for i in range(1000):
            digest = hashlib.sha256(concat.encode('utf-8')).hexdigest()

        if digest == results[0][1]:
            print("User is present, password is valid")
            return True

        else:
            return False
    else:
        return False
    conn.commit()


if __name__ == '__main__':
    args = parse_args()
    open_and_create()
    if args.u and args.p:
        save_new_username_correct(args.u, args.p)
    elif args.c and args.p:
        check_for_username_correct(args.c, args.p)
    conn.close()
