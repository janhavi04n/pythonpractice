# -*- coding: utf-8 -*-
#import mysql.connector
from mysql.connector import connect, Error
import getpass

#usr = input('enter db username : ')
#pwd = getpass.getpass(prompt='enter password : ')
query = 'select book_id, title, author, genre from BOOKS'

try:
    with connect(
        host = "localhost",
        user = 'janhavi',
        password = 'silverSt0ne',
        db = "library_db"
        ) as connection:
            #print(connection)
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                for row in result:
                    print(row)
    connection.close()
except Error as e:
    print(e)
