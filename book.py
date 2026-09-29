# holds book class for organizing books
# will eventually take in input from user

class Book:
    def __init__(self, title, series="", book_num=1, date_started="", date_finished="", read_count=0, summary="", ranking=0):
        self.title = title
        self.series = series
        self.book_num = book_num
        self.date_started = date_started
        self.date_finished = date_finished
        self.read_count = read_count
        self.summary = summary
        self.ranking = ranking # out of 10

    