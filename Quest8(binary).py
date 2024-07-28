# Ques - check wheather the input number comes in 2's power or not

number = int(input("Enter the number : "))

if number == 0:
  print("false")
elif number == 1:
  print("true")

while number > 1:
  if number % 2 != 0:
    print("false")
    break
  number = number // 2
else:
     print("true")




print("*********************************************************")

# another mmethod using binary and bitwise operation

def ispowerOfTwo(n):
    cnt = 0
    while n > 0:
        if((n & 1) == 1):
          cnt+= 1
        n = n >> 1
    if cnt == 1:
        return True

    return False
n= int(input())
print(ispowerOfTwo(n))
