#!/usr/bin/env python

import math



class trigonometry(object):


    def __init__(self, d="undefined"): #Angles in degrees

        if d!="undefined":
            self.degree = d
            self.housekeeping() # if the degrees are less than 0 this function makes it more than 0
            self.radian = (self.degree * math.pi) / 180


        self.accuracy = 20 # It is not percentage and I suggest you keep the value above 9 and you could even increase it to infinity but it's only going
                           # to be slower
        self.sign = 0 # 0 = negative and 1 = positive
        if d!="undefined":
            self.vos = self.sine() #vos = value of sign
        #print(d)


    def swap(self): # swaps sign to opposite value
        self.sign = 1 if self.sign == 0 else 0

    def sine(self, d="undefined"):
        if d != "undefined":
            d = self.housekeeping(d)
            self.radian = (d * math.pi) / 180

        r = self.radian

        self.sign = 0 # initiate sign to negative
        self.sinev = r
        for i in range(2, self.accuracy):
            if i % 2 != 0:
                if self.sign == 0:
                    self.sinev -= r**i/math.factorial(i)
                    self.swap()
                else:
                    self.sinev += r**i/math.factorial(i)
                    self.swap()

        if self.quadrant > 2:
            self.sinev = -1 * self.sinev
        return self.sinev

    def cos(self, d="undefined"):

        if d!="undefined":
            d = self.housekeeping(d)
            sine = self.sine(d)
        else:
            sine = self.vos  # vos = value of sine
        #if type(sine) == type(6.6):

        cos = math.sqrt(1-(sine**2))
        return cos

    def tan(self, d="undefined"):
        if d!="undefined":
            d = self.housekeeping(d)
            cos_val = self.cos(d)
            self.vos = self.sine(d)
        else:
            cos_val = self.cos()
        if cos_val == 0:
            return "undefined"
        return self.vos / cos_val


    def cot(self, d="undefined"):

        if d!="undefined":
            d = self.housekeeping(d)
            tan_val = self.tan(d)
        else:
            tan_val = self.tan()
        if tan_val == 0 or tan_val == "undefined":
            return "undefined"
        return 1/tan_val

    def csc(self, d="undefined"):

        if d!="undefined":
            d = self.housekeeping(d)
            sine_val = self.sine(d)
        else:
            sine_val = self.vos
        if sine_val == 0:
            return "undefined"
        return 1/sine_val

    def sec(self,d="undefined"):

        if d!="undefined":
            d = self.housekeeping(d)
            cos_val = self.cos(d)

        else:
            cos_val = self.cos()
        if cos_val == 0:
            return "undefined"
        return 1/cos_val


    def housekeeping(self, d="undefined"): # plays with degree to simplify it to a smaller or
                                            # higher value depending on the situation

        if(d!="undefined"):
            self.degree = d

        while self.degree < 0:
            self.degree += 360

        if self.degree > 360:
            self.degree = self.degree % 360



        if self.degree >= 0 and self.degree <= 90:
            self.quadrant = 1
        elif self.degree > 90 and self.degree <=180:
            self.quadrant = 2
        elif self.degree > 180 and self.degree <=270:
            self.quadrant = 3
        elif self.degree > 270 and self.degree <=360:
            self.quadrant = 4


        if self.degree > 90 and self.degree <= 180:
            self.degree = 180 - self.degree
        if self.degree > 180 and self.degree <= 270:
            self.degree = self.degree - 180
        if self.degree > 270 and self.degree<=360:
            self.degree = 360 - self.degree



        return self.degree
