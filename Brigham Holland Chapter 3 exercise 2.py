#Brigham Holland Chapter 3 exercise 2
hours = input('Enter Hours: ')
try:
  float(hours) >= 0
except: 
  print ('Error, please ener numeric input')
  hours = input('Enter Hours: ')

rate = input('Enter Rate: ')
try :
  float(rate) >= 0
except: 
    print ('error, please enter numeric input')
    rate = input('Enter Rate: ')
hours = float(hours)
rate = float(rate)

if hours >= 40 :
  extra_time = hours - 40
else: 
    extra_time = 0
extra_pay = 0.5 * rate * extra_time

pay = hours * rate + extra_pay
print (pay)
