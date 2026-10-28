""" A Python program that checks whether a number is a power of 4 using recursion, 
repeatedly divides by 4, and stops when it reaches either the True base case or a False stopping condition."""

def powerOf4Check(num):    
    if num == 1:
        return True

    if num <= 0 or num % 4 != 0:
        return False

    return powerOf4Check(num // 4)

print(powerOf4Check(64))
