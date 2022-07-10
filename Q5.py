#Q5

def calculateNumbersSum():
    sum = 0
    for number in range(10,1000000):
        digit_sum = 0
        for j in str(number):
            digit_sum+= int(j)**5

        if(digit_sum==number):
            print(number,end=" ")
            sum+=number

    return sum 

#driver code

sum = calculateNumbersSum()
print("sum = "+ str(sum))