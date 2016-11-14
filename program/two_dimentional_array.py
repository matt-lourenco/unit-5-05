# Created on 14 Nov 2016
# Created by: Matthew Lourenco
# This is a program that lets you input a 2 dimentional array then finds the average of the randomly generated numbers

from numpy import random

def add_elements(array):
    average = 0
    for find_row in array:
        for find_coloumn in find_row:
            average = average + find_coloumn
    average = average / (len(array[0]) * len(array))
    return average

number_rows = raw_input('Enter the number of rows: ')
number_rows = int(number_rows)
number_coloumns = raw_input('Enter the number of coloumns: ')
number_coloumns = int(number_coloumns)
chart = []
for row in range(0, number_rows):
    chart.append([])
    for coloumn in range(0, number_coloumns):
        chart[row].append(random.randint(1, 51))
print(chart)
chart_average = add_elements(chart)
print('Average -> ' + str(chart_average))
