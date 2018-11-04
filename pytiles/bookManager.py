import pandas as pd
import json

class Book:
    def __init__(self, book_id, name, author, price):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.price = price

    def getBookID(self):
        return self.book_id

    def getName(self):
        return self.name

    def getAuthor(self):
        return self.author

    def getPrice(self):
        return self.price

    def setBookID(self, book_id):
        self.book_id = book_id
        return ''

    def setName(self, name):
        self.name = name
        return ''

    def setAuthor(self, author):
        self.author = author
        return ''

    def setPrice(self, price):
        self.price = price
        return ''

    def __str__(self):
        return "Book id: {0}, name:{1}, author:{2}, price:{3}".format(self.book_id, self.name, self.author, self.price)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    def toObject(self):
        return json.loads(self,)

def getBooks():
    try:
        with open('data.txt') as json_file:  
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        return [{}]

def addBook(book_id, name, author, price):
    
    book = Book(book_id, name, author, price)
    data = {}
    data['books'] = []
    data['books'].append(book.toJSON())
    with open('data.txt', 'w') as outfile:  
        json.dump(data, outfile)
        # outfile.write(data)
    data = getBooks()
    print(data)
    s = json.load(data)


    print("{0}".format(s['author']))


addBook('book_1','WOF','Kalam',100)