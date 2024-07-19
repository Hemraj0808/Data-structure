# Ques2 - write a python program to calculate a decimal number of the given binary value

binary_number = int(input("Enter the binary number : "))
result = 0
power = 0
while binary_number >0:
    result  += (binary_number % 10) * (2 ** power)
    power += 1
    binary_number = binary_number // 10

print(result)
