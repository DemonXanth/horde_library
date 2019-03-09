import sqlite3
import isbnlib
from all import *

db = sqlite3.connect('test.db')
db.row_factory = sqlite3.Row
cursor = db.cursor()

while(True):
    print("What do you want to do? \nYou can use commands init, read, add, delete, search, and quit")
    c1 = input(':')
    print('\n')
    c1 = c1.lower()

    if c1 == 'init' or c1 == 'i':
        initDB(cursor)

    elif c1 == 'read' or c1 == 'r':
        readAll(cursor)

    elif c1 == 'add' or c1 == 'a':
        isbn = input('ISBN of the book you would like to add: ')
        add(cursor, isbn)

    elif c1 == 'delete' or c1 == 'd':
        id = input('ID of book you would like to delete: ')
        delete(cursor, id)

    elif c1 == 'search' or c1 == 's':
        print("You can search by ID, ISBN, Title, Author, Year, or Publisher")
        c2 = input(':')
        c2 = c2.lower()
        if c2 == 'id':
            id = input('ID you would like to search by: ')
            printRows(search_equals(cursor, 'ID', id))

        elif c2 == 'isbn' or c2 == 'i':
            isbn = input('ISBN you would like to search by: ')
            printRows(search_equals(cursor, 'ISBN', isbn))

        elif c2 == 'title' or c2 == 't':
            title = input('Title you would like to search by: ')
            # printRows(search_like(cursor, 'Title', title))

        elif c2 == 'author' or c2 == 'a':
            author = input('Author you would like to search by: ')
            # printRows(search_like(cursor, 'Author', author))

        elif c2 == 'publisher' or c2 == 'p':
            publisher = input('Publisher you would like to search by: ')
            # printRows(search_like(cursor, 'Publisher', publisher))

        elif c2 == 'year' or c2 == 'y':
            year = input('Year you would like to search by: ')
            # printRows(search_like(cursor, 'Year', year))

        else:
            print("Not a valid input")

    elif c1 == 'quit' or c1 == 'q':
        c3 = input('Do you want to save your changes? Y/n: ')
        if c3 == '' or c3.lower() == 'y':
            db.commit()
        db.close()
        break

    else:
        print('Not a valid input')
