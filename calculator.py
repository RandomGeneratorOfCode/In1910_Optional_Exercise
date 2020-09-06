import numpy as np

def add(x, y):
    return x + y

def factorial(n):
    assert n >= 0, 'value cant be less then 0'
    sum = 1
    for i in range(1,n+1):
        sum = sum * i
    return sum

def sin(x,n):
    sum = 0
    for i in range(n+1):
        sum = sum + ((-1)**i*x**(2*i + 1))/(factorial(2*i + 1))
    return sum

def divide(x,y):
    return x/y

def subtract(x,y):
    return x - y

def multi(x,y):
    return x * y
