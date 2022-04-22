#first, we will take the input

lower_input = int(input("plese, enter the lowest range valu: "))
upper_input = int(input("please, enter the upper renge valu: "))

print("the prime number in the range are : ")

for number in range(lower_input, upper_input +1):
    if number > 1:
        for i in range(2, number):
            if (number % 2) == 0:
                break
        else:
            print(number)