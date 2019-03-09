import sqlite3
import isbnlib
# from app import app

# db = sqlite3.connect('test.db')
# db.row_factory = sqlite3.Row
# cursor = db.cursor()


def initDB(cursor):
    cursor.execute("""CREATE TABLE all_books(
        ISBN NOT NULL,
        Title TEXT NOT NULL,
        Author TEXT NOT NULL,
        Year TEXT NOT NULL,
        Publisher TEXT NOT NULL,
        Added TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        SmallPic TEXT,
        Pic TEXT
        )""")


def add(cursor, isbn):
    if isbnlib.is_isbn13(isbn):
        info = isbnlib.meta(isbn)
        au = ", ".join(info['Authors'])
        addBook(cursor, info['ISBN-13'], info['Title'],
                au, info['Year'], info['Publisher'], getCoverSmall(isbn), getCover(isbn))

        printRows(search_equals(cursor, 'ISBN', isbn))
    else:
        print("Not a valid ISBN")


def readAll(cursor):
    for row in cursor.execute("SELECT * FROM all_books"):
        printRow(row)


def search_equals(cursor, key, data):
    command = "SELECT * FROM all_books WHERE " + key + "=(?)"
    cursor.execute(command, (data, ))
    return cursor.fetchall()


def search_like(key, data):
    db = sqlite3.connect('test.db')
    db.row_factory = sqlite3.Row
    cursor = db.cursor()

    Data = '%' + data + '%'
    command = "SELECT * FROM all_books WHERE " + key + " LIKE (?)"
    cursor.execute(command, (Data, ))
    return cursor.fetchall()


def printRow(row):
    if row == []:
        print('There is no book with that value')
    else:
        print("ID: " + str(row['ID']) + "\n" +
              row['Title'] + "\n" +
              'By: ' + row['Author'] + "\n" +
              "ISBN: " + row['ISBN'] + "\n" +
              "Made In: " + row['Year'] + "\n" +
              'Published By: ' + row['Publisher'] + "\n" +
              "Added: " + row['Added'] + "\n")


def printRows(rows):
    for row in rows:
        printRow(row)


def delete(cursor, id):
    cursor.execute("DELETE FROM all_books WHERE ID = (?)", (id, ))
    print("Book with ID " + id + " is deleted")


def addBook(cursor, isbn, title, author, year, publisher, smallPic, pic):
    cursor.execute("INSERT INTO all_books(ISBN, Title, Author, Year, Publisher, SmallPic, Pic) values((?), (?), (?), (?), (?), (?), (?))",
                   (isbn, title, author, year, publisher, smallPic, pic))


def getCoverSmall(isbn):
    cover = isbnlib.cover(isbn)
    if cover != None:
        return cover['smallThumbnail']


def getCover(isbn):
    cover = isbnlib.cover(isbn)
    if cover != None:
        return cover['thumbnail']
