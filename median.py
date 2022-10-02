"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers.sort()
        listLen = len(numbers)
        print(listLen)
        if(listLen % 2 == 0):
            median = (numbers[int(listLen / 2)] + numbers[int(listLen / 2 - 1)]) / 2
            print(median)
        else: 
            median = numbers[int(listLen / 2)]
            print(median)
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
#print(numbers)