class Time:
    def __init__(self, h = 0, m = 0):
        self.hours = h
        self.minutes = m
    
    def __str__(self):

        timestring = f"{self.hours}:{self.minutes}"

        if self.hours < 10:
            timestring = "0" + timestring
        if self.minutes < 10:
            timestring = timestring[:3] + "0" + timestring[3:]
        
        return timestring
    
    def __repr__(self):
        return self.__str__()
    
    def __lt__(self, other):
        return self.hours * 60 + self.minutes < other.hours * 60 + other.minutes
    
    def __gt__(self, other):
        return self.hours * 60 + self.minutes > other.hours * 60 + other.minutes
    
    def __eq__(self, other):
        return self.hours * 60 + self.minutes == other.hours * 60 + other.minutes
    
    def addMin(self, m):

        self.minutes += m
        self.hours += self.minutes // 60
        self.minutes %= 60

    def __add__(self, other):
        return Time(0, self.minutes + other.minutes + (self.hours + other.hours))
    
    def __sub__(self, other):
        return Time(0, self.minutes - other.minutes + (self.hours - other.hours))
    
    def now(): # not a required thing, bonus task i made myself do
        import time
        t = time.localtime()
        return Time(t.tm_hour, t.tm_min)
    
class Date(Time):
    def __init__(self, h=0, m=0, d=1, mo=1, y=2000):
        super().__init__(h, m)
        self.day = d
        self.month = mo
        self.year = y
    
    def __str__(self):
       return f"{self.day}.{self.month}.{self.year} " + super().__str__()
    
    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        return Date(0, 0, self.day + other.day, self.month + other.month, self.year + other.year)
    
    def daysUntil(self, other):
        if self.year > other.year or self.month > other.month or self.day > other.day:
            return -1
        else:
            return (other.year - self.year) * 365 + (other.month - self.month) * 30 + (other.day - self.day)

    def inNDays(self, n): # NOTE; 31.12.2020 + 1 day = 1.1.2021

        import datetime

        date = datetime.datetime(self.year, self.month, self.day)
        date += datetime.timedelta(days=n)

        d = date.day
        m = date.month
        y = date.year

        return Date(0, 0, d, m, y)


a = Date(12, 30, 1, 1, 2020)
b = Date(12, 0, 1, 1, 1936)
c = Date(12, 30, 31, 12, 2020)