import datetime
from trigonometry import trigonometry
import math

class calculator(object):

    def __init__(self, birthDay=(0,0,0)):

        self.date = datetime.date
        self.trigonometry = trigonometry() # for speed optimization
        if birthDay[0] != 0:
            self.setBirthday(birthDay)

    def setBirthday(self, birthday):

        self.birthYear = birthday[0]
        self.birthMonth = birthday[1]
        self.birthDay = birthday[2]
        if(self.birthYear>=datetime.datetime.today().year):
            raise ValueError("Invalid year of birth.")
        self.that_day = \
            self.date(self.birthYear, self.birthMonth, self.birthDay)

    def theIntelligence(self, another_day):

        # another_day is expected to be tuple containing day in the format
        # (years, months, days)
        days = self.daysSinceBirth(another_day)
        degrees = round(360*days/33, 2)
        #If degrees is > 360 decrease it
        return self.trigonometry.sine(degrees)

    def daysSinceBirth(self, another_day):

        another_day = self.date(another_day[0],another_day[1],another_day[2])
        differentiated_day = another_day - self.that_day
        return differentiated_day.days


        
    
