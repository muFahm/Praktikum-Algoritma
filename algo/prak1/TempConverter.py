# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 16:26:44 2022

@author: fhm

This code is for 'Tugas Praktikum'
"""

# Temperature conversion program (celcius-fahrenheit) vice versa

# Display program welcome
print('this program will convert c to f vice versa')
print('(F) to convert f to c')
print('(C) to convert c to f')

# Get temperature to convert
which = input('Enter Selection: ')
temp = int(input('Enter temp to convert: '))

# Determine temperature conversion needed and show theresult
if which == 'F' or 'f':
    converted_temp = (temp -32) * 5/9
    print(temp, 'degrees f  equals', converted_temp, 'degrees c')
else:
    converted_temp = (9/5 * temp) + 32
    print(temp, 'degrees c  equals', converted_temp, 'degrees f')