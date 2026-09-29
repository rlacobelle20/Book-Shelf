# holds book class for organizing books
# will eventually take in input from user

class Book:
    def __init__(self, title="", author=[], year=2000, publisher="", series="", book_num=1, date_started="", date_finished="", read_count=0, summary="", ranking=0):
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher
        self.series = series
        self.book_num = book_num
        self.date_started = date_started
        self.date_finished = date_finished
        self.read_count = read_count
        self.summary = summary
        self.ranking = ranking # out of 10

    # all the update functions
    def update_title(self, new_title):
        self.title = new_title

    # allows for multiple authors
    def update_author(self, new_author):
        self.author.append(new_author)

    def update_year(self, year):
        self.year = year

    def update_publisher(self,publisher):
        self.publisher = publisher

    def update_series(self, series):
        self.series = series

    def update_book_num(self, book_num):
        self.book_num = book_num

    def update_date_started(self, date_start):
        self.date_started = date_start

    def update_date_finished(self, date_end):
        self.date_finished = date_end

    def update_read_count(self, count):
        self.read_count = count

    def update_summary(self, summary):
        self.summary = summary

    def update_ranking(self, ranking):
        self.ranking = ranking



        

    