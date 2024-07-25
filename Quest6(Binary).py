# Quest - write a python program to calculate hexadecimal value for  a given decimal number


list = []
number = int(input("Enter the number : "))
if number == 0:
    print(0)
while number > 0:
    a= number % 16
    list.append(a)
    number = number // 16

    if a >= 10:
      alphabet = ["A","B","C","D","E","F"]
      list[list.index(a)] = alphabet[a-10]

list.reverse()
for i in list:
  print(i, end="")