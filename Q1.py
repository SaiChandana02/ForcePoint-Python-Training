#Algorithm to reverse the character array.

from ast import main

def reverse (array):
    i = 0
    j = len(array)-1
    while i<j:
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
        i+=1
        j-=1
        return array


charArray = ['a','b','c','d']
print(charArray)
reverse(charArray)
print(charArray)

