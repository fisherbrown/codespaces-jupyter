# Fisher Brown
# Lab Section# 10
# 4 Nov 24
# Worked with Jayden Robison



numofdays = [31,28,31,30,31,30,31,31,30,31,30,31]

days = {'sunday' : 0, 'monday' : 1, 'tuesday' : 2, 'wednesday' : 3, 'thursday' : 4, 'friday' : 5, 'saturday' : 6}

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        numofdays[1] = 29 
    else:
        numofdays[1] = 28
def first_jan(year):
    y = year - 1
    day_one = (36+y+(y//4)-(y//100)+(y//400))%7
    return day_one
def valid_date(month,day,day_one):
    if day > numofdays[month - 1] or day <= 0:
        print('Not a valid date')
        return None
    totaldays = sum(numofdays[:month - 1]) + day
    dayofweek = (totaldays + day_one - 1) % 7  
    return dayofweek


date = input('enter a date of the format MM/DD/YYYY: ')

month = int(date[0:2])

day = int(date[3:5])

year = int(date[6:11])        


leap_year(year)
day_one = first_jan(year)
dayofweek = valid_date(month,day,day_one)
weekday = 1
if dayofweek is not None:
    for key,value in days.items():
        if dayofweek == days[key]:
            print(f'{date} {key}')

      