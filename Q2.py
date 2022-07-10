#Find the occurence of each number from the array

#function
def numberOfOccurences(array):
    occurence = [0]*101    # creating an array of size 101 to store occurence.
    for ele in array:
        occurence[ele]+=1

    return occurence


#driver code
numberArray = [1,5,6,7,8,100,99,98,52,64,68,23,58,32,6,88,74,32,100,1,5,68,74,52,98,99]
occurence = numberOfOccurences(numberArray)
print(numberArray)
print(occurence)
