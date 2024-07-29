# check the i'th bit is set or not (set means 1 and not set means 0)

number = int(input("Enter the number : "))
position = int(input("Enter the position : "))

list = []
if number == 0:
    print(0)
while number > 0:
    a= number % 2
    list.append(a)
    number = number // 2
# list.reverse()

# print(list)

if list[position] == 1:
    print("True")
else:
    print("False")





print("*************************************************")

# ANOTHER METHOD

n,pos=map(int,input().split())
if((n>>pos)&1==1):
    print("True")
else:
    print("False")