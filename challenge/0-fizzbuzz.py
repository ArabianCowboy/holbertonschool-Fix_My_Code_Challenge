#!/usr/bin/env python3
import sys

def fizzbuzz(n):
    for i in range(1, n + 1):
        end = "\n" if i == n else " "
        if i % 15 == 0:
            print("FizzBuzz", end=end)
        elif i % 3 == 0:
            print("Fizz", end=end)
        elif i % 5 == 0:
            print("Buzz", end=end)
        else:
            print(i, end=end)

if __name__ == "__main__":
    fizzbuzz(int(sys.argv[1]))
