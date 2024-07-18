# Ques1 - write a python program to calculate binary  value of the given deciaml number

list = []
number = int(input("Enter the number : "))
if number == 0:
    print(0)
while number > 0:
    a= number % 2
    list.append(a)
    number = number // 2
list.reverse()
for i in list:
  #print(i, end="")
  print(i)
#print(list)



# in built method for binary number is  = bin()