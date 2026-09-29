# contains 1 or more books in it
from book import *

class Library:
    def __init__(self, books=[]):
        self.books = books

    # add one book to the library
    def add_book(self, book):
        self.books.append(book)

    # add more than one books into the library
    def add_multiple_books(self, book):
        self.books.extend(book)

    # removes specific book
    def delete_book(self, book):
        self.books.remove(book)

    # removes multipe books
    def delete_multiple_books(self, book):
        for b in book:
            # make sure b exists in library
            if b in self.books:
                self.books.remove(b)

    # average ranking for books overall
    def average_ranking(self):
        avg = 0
        for book in self.books:
            avg += book.ranking
        return avg / len(self.books)

    # counts all unique authors
    def author_count(self):
        authors = dict() # author (string): count (int)
        for b in self.books:
            if b.author not in authors:
                authors[b.author] = 1
            else:
                authors[b.author] += 1
        return authors