#Given two sorted arrays in ascending order,write a function which takes both as inputs and return an array of common elements



def mergeSortedArray(array1,array2):
    i=0
    j=0
    mergedArray = []
    n = len(array1)
    m = len(array2)
    while(i<n or j<m):
        if(array1[i]==array2[j]):
            mergedArray.append(array1[i])
            i+=1
            j+=1
        elif(array1[i]>array2[j]):
            j+=1
        else:
            i+=1
    return mergedArray

array1 = [1,4,6,9,10]
array2 = [2,4,6,8,10]

mergedArray = mergeSortedArray(array1,array2)
print(array1)
print(array2)
print(mergedArray)
