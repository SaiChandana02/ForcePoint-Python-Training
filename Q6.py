#Write a function that takes in an integer array and returns the item that occurs the most

#function
def maxOccurence(array):
    occurence = [0]*101    # creating an array of size 101 to store occurence.
    ans = 0
    ansFreq = 0
    for ele in array:
        occurence[ele]+=1
    for index, ele in enumerate(occurence):
        if ele>=ansFreq:
            ans = index
            ansFreq = ele

    return ans

#driver code
numberArray = [1,5,6,7,8,100,9,98,52,64,68,23,58,32,6,88,74,32,10,1,5,68,74,52,8,99,99,74]
maxOccurenceNumber = maxOccurence(numberArray)
print(numberArray)
print(maxOccurenceNumber)