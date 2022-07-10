#round off a float number having only one decimal place 

def convertFloatToInt(floatNum):
    temp = floatNum*10
    firstNum = int(temp/10)
    secondNum = temp%10
    if(secondNum>5):
        firstNum+=1
    return firstNum

#driver code

num = 6.7
intNum = convertFloatToInt(num)
print(num)
print(intNum)