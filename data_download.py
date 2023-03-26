#!/usr/bin/env python3

#Imports
import csv
import pprint
import matplotlib.pyplot as plt
import numpy as np

#set up dictionary
data_dict = {}
IN_dict = {}
GA_dict = {}
nested_state_dict = {}

count = 0

for line in open('/Users/richardmcmanjus/Documents/College/Datafest/Data/categories.csv'):
#    data = line.rstrip()
    data = line.split(',')
    if data[1] == 'IN':
        if not data[2] in IN_dict:
            IN_dict[ data[2] ] = 0

    if data[1] == 'GA':
        if not data[2] in GA_dict:
            GA_dict[ data[2] ] = 0

pprint.pprint(IN_dict)
pprint.pprint(GA_dict)


for line in open('/Users/richardmcmanjus/Documents/College/Datafest/Data/questions.csv'):
    data = line.split(',')
    if data[9] == 'NULL':

        if data[1] == 'IN':
            IN_dict[ data[3] ] += 1

        if data[1] == 'GA':
            GA_dict[ data[3] ] += 1


pprint.pprint(IN_dict)
pprint.pprint(GA_dict)

# state_dict[ data[1] ] = state_dict.get( data[1], 0 ) + 1

#Loop through dictionarys to create a list
IN_list_value = []
IN_list_key = []
GA_list_value = []
GA_list_key = []
for key, value in sorted(IN_dict.items()):  
    IN_list_value.append( value )
    IN_list_key.append( key   )

for key, value in sorted(GA_dict.items()):
    GA_list_value.append( value )
    GA_list_key.append( key   )

print( IN_list_value )
print( IN_list_key   )
print( GA_list_value )
print( GA_list_key   )

#Make py charts

categories_list = {'Consumer Financial Questions'}

plt.pie( IN_list_value, labels=IN_list_key )
plt.show()


#load in state dictionary
'''
for index in data_dict:
    if not index in state_dict:
        state_dict[index] = 
for key, value in data_dict.items():
    print(f'{key} : {value}')
'''
 

