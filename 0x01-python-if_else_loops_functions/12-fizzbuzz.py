#!/usr/bin/python3
def fizzbuzz():
    for _ in range(1, 101):
        if _ % 3 == 0 and _ % 5 == 0:
            print("FizzBuzz", end=" ")
        elif _ % 3 == 0:
            print("Fizz", end=" ")
        elif _ % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(_, end=" ")