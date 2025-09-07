n=int(input("enter a number: "))
def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
result=factorial(n)
print(f"the factorial of {n} is :{result}")

from math import *
n=int(input("enter a number: "))
print("square root: ",sqrt(n))
print("logarithm: ",log(n))
print("sine :"sin(n))
