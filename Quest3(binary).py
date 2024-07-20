# Ques3 - convert decimal to octal

list = []
number = int(input("Enter the number : "))
if number == 0:
    print(0)
while number > 0:
    a= number % 8
    list.append(a)
    number = number // 8
list.reverse()
for i in list:
  print(i, end="")
#print(list)
