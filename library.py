# contains 1 or more books in it

class Library:
    def __init__(self, books={}):
        self.books = books

    def average_ranking(self):
        avg = 0
        for book in self.books:
            avg += book.ranking
        return avg