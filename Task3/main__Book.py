import Book

def main():
    print("{:^54}".format("Variant 9 Tsiupka Denis IPZ/R-18k"))
    print("{:^54}".format("Base book:"))
    bookBase = Book.Book()
    # methods
    bookBase.getInfo()
    print("Years passed from publication a book: {}".format(bookBase.getAgeYearBook()))
    print("Days passed from publication a book: {}".format(bookBase.getAgeDayBook()))

    print("{:^54}".format("User book:"))
    userBook = Book.Book()
    userBook.nameBook = input("Enter your book name: ")
    userBook.yearPublication = int(input("Enter a year publication for your book:"))
    userBook.getInfo()
    print("Years passed from publication a book: {}".format(userBook.getAgeYearBook()))
    print("Days passed from publication a book: {}".format(userBook.getAgeDayBook()))


if __name__ == '__main__':
    main()
