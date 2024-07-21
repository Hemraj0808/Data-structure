# convert Ocatal to decimal

Octal_number = int(input("Enter the binary number : "))
result = 0
power = 0
while Octal_number >0:
    result  += (Octal_number % 10) * (8 ** power)
    power += 1
    Octal_number = Octal_number // 10

print(result)