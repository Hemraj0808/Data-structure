# Ques - Two different integer k and n , find sum of the 2 power k and 2 power n using bitwise operator

k,n = map(int,input("Enter the k and n : ").split())


# 2^k is represented by shifting 1 left by k positions
power_k = 1 << k
# 2^n is represented by shifting 1 left by n positions
power_n = 1 << n

# Sum of 2^k and 2^n using bitwise OR
result = power_k | power_n
print(result)
