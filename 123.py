# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 17:34:29 2017

@author: kazIm
"""

# O(n log n)

def count_inversion(lst):
    return merge_count_inversion(lst)[1]

def merge_count_inversion(lst):
    if len(lst) <= 1:
        return lst, 0
    middle = int( len(lst) / 2 )
    left, a = merge_count_inversion(lst[:middle])
    right, b = merge_count_inversion(lst[middle:])
    result, c = merge_count_split_inversion(left, right)
    return result, (a + b + c)

def merge_count_split_inversion(left, right):
    result = []
    count = 0
    i, j = 0, 0
    left_len = len(left)
    while i < left_len and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += left_len - i
            j += 1
    result += left[i:]
    result += right[j:]
    return result, count        


#test code
fname = 'C:/Users/kazIm/Desktop/DataScience/IntegerArray.txt'

with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

#print(content)        


    
input_array_1 = []  #0
input_array_2 = [1,] #0
input_array_3 = [1, 5]  #0
input_array_4 = [4, 1] #1
input_array_5 = [4, 1, 2, 3, 9] #3
input_array_6 = [4, 1, 3, 2, 9, 5]  #5
input_array_7 = [4, 1, 3, 2, 9, 1]  #8

print(content[0:5])
print (count_inversion(content))
print (count_inversion(input_array_2))
print (count_inversion(input_array_3))
print (count_inversion(input_array_4))
print (count_inversion(input_array_5))
print (count_inversion(input_array_6))
print (count_inversion(input_array_7))
