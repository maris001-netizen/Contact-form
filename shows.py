import sqlite3
db = sqlite3.connect("shows.db")
cursor = db.cursor()
title = input("title:")
cursor.execute("SELECT * FROM shows WHERE title = ?", (title,))
rows = cursor.fetchall()
if rows:
    for row in rows:
        print(f"title: {row[0]}, year: {row[1]}, rating: {row[2]}")
    else:
        print("No shows found with that title.")