#!/usr/bin/python3
<<<<<<< HEAD
"""Script that lists all states from the DB."""
=======
"""Lists all states from the DB."""
>>>>>>> fdf18b6fab8375e89fd798686f733c098325ac33


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                   (argv[4],))
    myli = cursor.fetchall()
    for i in myli:
        print(i)
    cursor.close()
    db.close()
