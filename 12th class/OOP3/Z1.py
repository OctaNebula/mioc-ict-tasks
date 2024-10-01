class Time:
    def __init__(self, h, m):
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