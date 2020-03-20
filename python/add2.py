import os 
import sys

def add2(num1, num2):
    result = num1 + num2
    return result

def displayResult(num):
    print(num)

def test_add2():
    assert add2(2,2) == 4

if __name__ == "__main__":
    number = add2(3,2)
    displayResult(number)
