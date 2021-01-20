import datetime
from datetime import date


class Book(object):
    __slots__ = ['__nameBook','__yearPublication']

    def __init__(self, nameBook="World and War", yearPublication=1869):
        if not isinstance(nameBook, (str)):
            raise TypeError('Error: value is incorrect (must be str)')
        if not isinstance(yearPublication, (int)):
            raise TypeError('Error: value is incorrect (must be int or float)')
        self.__nameBook = nameBook
        self.__yearPublication = yearPublication

    @property
    def nameBook(self):
        print(1)
        return self.__nameBook

    @nameBook.setter
    def nameBook(self, value):
        if not isinstance(value, (str)):
            raise TypeError('Error: value is incorrect (must be str)')
        self.__nameBook = value

    @property
    def yearPublication(self):
        return self.__yearPublication;

    @yearPublication.setter
    def yearPublication(self, value):
        if not isinstance(value, (int)):
            raise TypeError('Error: value is incorrect (must be int or float)')
        self.__yearPublication = value

    def getInfo(self):
        print('\n<---------------- GET INFO FOR BOOK ---------------->\nA book name: {}\nA publication year: {}'.format(
            self.__nameBook, self.__yearPublication))
        return 1

    def getAgeDayBook(self):
        yearPublication = self.__yearPublication
        dateYearPublication = date(yearPublication, 1, 1)
        dateYearNow = date.today()
        days = (dateYearNow - dateYearPublication).days
        if (days >= 0):
            return days
        else:
            '\n<---------------- ERROR ---------------->\ndateYearNow - dateYearPublication < 0\n{} - {} = {}'.format(
                dateYearPublication, dateYearNow, dateYearNow - dateYearPublication)

    def getAgeYearBook(self):
        yearPublication = self.__yearPublication
        yearNow = datetime.date.today().year
        if (yearNow - yearPublication >= 0):
            return yearNow - yearPublication
        else:
            '\n<---------------- ERROR ---------------->\nyearNow - yearPublication < 0\n{} - {} = {}'.format(
                yearPublication, yearNow, yearNow - yearPublication)
