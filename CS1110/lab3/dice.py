"""
A simple die roller

Author: Richie Sun
Date: 09/02/21
"""
import random
first=int(input('Type the first number: '))
last=int(input('Type the last number: '))
print('Choosing two numbers between '+str(first)+' and '+str(last)+'.')
a=random.randint(first,last)
b=random.randint(first,last)
roll=a+b
print('The sum is '+str(roll)+'.')
