# -*- coding: utf-8 -*-
from builtins import input
from biorhythm import calculator
import datetime


def previous_and_next(iterable):
    iterator = iter(iterable)
    prev_item = None
    current_item = next(iterator)  # throws StopIteration if empty.
    for next_item in iterator:
        yield (prev_item, current_item, next_item)
        prev_item = current_item
        current_item = next_item
    yield (prev_item, current_item, None)
            
            
class pick_date(object):
    
        def __init__(self, input_data):
            self.ss = calculator()
            self.data = input_data
            self.today = datetime.datetime.today()
            output_datas = []
            for iteration in range(0, 366):
                current_data = self.create_data(iteration)
                prepared = (current_data)
                output_datas.append(prepared)
            self.output_datas = output_datas
                


        def create_data(self, i=0):
            
            today = self.today
            datas = []
            
            for bdays in self.data:
                
                self.ss.setBirthday(bdays)
                today = today + datetime.timedelta(days=i)
                datas.append( self.ss.theIntelligence( ( today.year, today.month\
                                                        , today.day ) ) )
            return datas
                
        def positivity(self, d):            
            n = 0
            for items in d:
                n += items # continue here, there is a bug that has to be fixed
                            # the percent is calculated in the basis of the sum 
                            # of number of students
            return  (n/len(d)) * 100


        def filter_out(self, data):
            highest = 0
            k = 0
            for key,value in data.items():
                if value > highest:
                    highest = value
                    k = key
                    
            return k
        
        def findTheRepeating(self, data):
            repeatDictionary = {}
            for count, items in enumerate(data):
                key = items[0]
                
                
                if key in repeatDictionary:
                    repeatDictionary[key] += 1
                else:
                    repeatDictionary[key] = 1
                

            return repeatDictionary

            
        def automate(self):
            output_data = self.output_datas
            datas = self.increasingStrategy(output_data)
            most_repeated_datas = self.filter_out(self.findTheRepeating(datas))
            found = []
            #print(datas)
            for items in datas:
                if items[0] == most_repeated_datas:
                    found = items[1:]
                    break
            self.printMe(most_repeated_datas)
            return most_repeated_datas
            
            
            
        @staticmethod       
        def increasingStrategy(data):
            current_element = 0
            approved = []
            for prev, curr, nxt in previous_and_next(data):
                
                increasing_items = 0
                if nxt == None or prev == None:
                    current_element += 1
                    continue
                for c, n in zip(curr, nxt):
                    if (n - c) > 0:
                        increasing_items += 1
                        approved.append( (current_element, curr) )
                current_element+=1
            return approved
            
            
        @staticmethod
        def numToDay(n):
            if n==1:
                return "January"
            elif n==2:
                return "February"
            elif n==3:
                return "March"
            elif n==4:
                return "April"
            elif n==5:
                return "May"
            elif n==6:
                return "June"
            elif n==7:
                return "July"
            elif n==8:
                return "August"
            elif n==9:
                return "September" 
            elif n==10:
                return "October"
            elif n==11:
                return "November"
            elif n==12:
                return "December"
                

        def printMe(self, d):
            date = self.today + datetime.timedelta(days=d)
            month =  self.numToDay(date.month)
            print("Start a advanced chapter at your class at %d of %s, %d"\
                  %(date.day, month, date.year) )
            return date


def get_input():
    birthday = []
    prompt = "y"
    print("Enter the birthday of your students in format year-month-day\n")
    while prompt == "y":
        b = input(">>>")
        b = str(b)
        
        splitted = b.split("-")

        birthday.append( (int(splitted[0]), int(splitted[1]), int(splitted[2]) ))
        prompt = input("\nDo you want to input more?(y/n):")
    return birthday
        
inputs = get_input()
works = pick_date(inputs)
date = works.automate()
