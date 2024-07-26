# Ques - write a python program to calculate a decimal value for a given hexadecimal number

def hex_to_dec(n_hex):
  n_hex=n_hex[::-1]
  hex_digit = "0123456789ABCDEF"
  power = 0; result = 0
  for ch in n_hex:
    result += hex_digit.index(ch) * 16 ** power
    power += 1
  return result

n_hex=input()
print(hex_to_dec(n_hex))