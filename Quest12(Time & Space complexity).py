'''Time complexity -- how many loops

space complexity -- how many variables'''


# Time complexity
n = int(input())
temp=n
c=1
for i in range(n):
  temp= n
  while temp != 1:
    print("hi")
    c += 1
    temp = temp // 2
print(c)