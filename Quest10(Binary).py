# change the bit acc.to user in the binary number and then calculate number

number = int(input("Enter the number : "))
position = int(input("Enter the position : "))

list = []
if number == 0:
    print(0)
while number > 0:
    a= number % 2
    list.append(a)
    number = number // 2
list.reverse()
print(list)

if list[position] == 1:
    list[position] = 0
else:
    list[position] = 1


for i in list:
  print(i, end="")

# incomplete


print("*************************************************")

# another method

n,pos=map(int,input().split(" "))
print(n|(1<<pos))