#!/usr/bin/env python

def fizzbuzz(num):
    if num % 15 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

value = int(input("How many values should we process? "))
numbers = range(1, value + 1)
for n in numbers:
    print(fizzbuzz(n))


