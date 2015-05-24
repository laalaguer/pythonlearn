# Knowledge points:
# 1. math module
# 2. for loop
# 3. common operations on numbers float(), round(), int() and abs()

# Expect user to input something, result is stored as a string
user_input = raw_input("Please input a sequence of numbers, like: 1 2 3.1 2.1 -3 9: \n")
# split it into a list sequence
numbers = user_input.strip().split(" ") # get rid of whitespace or \n at end. split the input string by space,

print "=== convert to float"
# iterate through, get each number operation
for number in numbers:
	print float(number)
print "=== convert to absolute"
# print the number absolute value:
for number in numbers:
	print abs(float(number))
print "=== convert to integer, and rounded"
# print the number rounded value:
for number in numbers:
	print int(round(float(number)))

import math
print "=== floored to nearest"
# print the number floored to the nearest integer
for number in numbers:
	print math.floor(float(number))
print "=== uplift to nearest"
# print the number uplift to the nearest integer
for number in numbers:
	print math.ceil(float(number))