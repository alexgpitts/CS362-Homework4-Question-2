'''
Author: Alex Pitts
Date: 2/7/21
Class: CS 362

Description: This program simply calculates average of all the elements in a list. 
             The function takes a list as an argument and calculates its average. 
'''

def average_of_list(list):    
    sum =0
    for i in list: 
        sum += i

    average = sum/len(list)
    return average

# print(average_of_list({1, 2}))