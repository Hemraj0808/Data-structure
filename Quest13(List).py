#. LIST


# Ques = write a program to find the sum of the elements in the given list only if the element is greater than all its previous elements

#list1 = list(map(int,input().split(" ")))
list2 = list(map(int,input().split()))
result = list2[0]
curr_max= list2[0]
for i in list2:
  if i > curr_max:
    result += i
    curr_max = i
print(result)
