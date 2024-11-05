# Fisher Brown
# Lab Section# 10
# 4 Nov 24



months = {'jan' : 31, 'feb' : 28, 'mar' : 31, 'apr' : 30, 'may' : 31, 'jun' : 30, 'jul' : 31, 
       'aug' : 31, 'sep' : 30, 'oct' : 31, 'nov' :30, 'dec': 31}

months_2 = {'jan' : 01, 'feb' : 02, 'mar' : 03, 'apr' : 04, 'may' : 05, 'jun' : 06, 'jul' : 07, 
       'aug' : 08, 'sep' : 09, 'oct' : 10, 'nov' : 11, 'dec': 12}

long_month = ['jan','mar','may','jul','aug','oct','dec'] 

days = {'sun' : 0, 'mon' : 1, 'tue' : 2, 'wed' : 3, 'thu' : 4, 'fri' : 5, 'sat' : 6}

date = input('enter a date of the format MM/DD/YYYY: ')

month = int(date[0:2])

day = int(date[3:5])

year = int(date[6:11])

ski = date.split('/')

def leap_year(year):
    if year % 100 == 0:
        print('not a leap year')
    elif year % 4 == 0:
        months['feb'] = 29
    else: 
        print('not a leap year')
def first_jan(year):
    y = year - 1
    day_one = (36+y+(y//4)-(y//100)+(y//400))%7
    return day_one
def valid_date(date):
    if ski[0] not in range(0,13):
        print('not good enough!!!')
    elif ski[1] = 31:
        

leap_year(year)
day_one = first_jan(year)

print(months)    
print(day_one)        