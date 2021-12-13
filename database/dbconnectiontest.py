import sqlite3

# this will create a sqlite db if it doesnt exist
# else will open the connection
db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts_list (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts_list (name, phone, email) VALUES ('Harry Kane', 222222, 'harrykane@hisemail.com')")

cursor = db.cursor()
cursor.execute("SELECT * from contacts_list")

for row in cursor:
    print(row)

db.close()

