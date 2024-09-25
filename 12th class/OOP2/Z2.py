import datetime

class DateV2(datetime.date):
    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d
        super().__init__()
    
    def __str__(self):
        return f"{self.y}-{self.m}-{self.d}"
    
    def __repr__(self):
        return f"DateV2({self.y}, {self.m}, {self.d})"
    
    def __add__(self, other):
        return DateV2.fromordinal(self.toordinal() + other.d)
    
    def __sub__(self, other):
        return self.toordinal() - other.toordinal()