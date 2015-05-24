# We try to improve the previous 'math_operation.py' by reduce the code
# here we introduce a concept named list-comprehensive
# Knowledge points:
# 1. list-comprehensive, the [x for x in a-list]
# 2. dir() function to get the current environment variable names in space.
# 3. "in" check, we never user string.search() in Java, but use "in" to check string existence.
# 4. "eval()" function to run the expression

# still, we expect user to input something
user_input = raw_input("Please input a sequence of numbers, like: 1 2 3.1 2.1 -3 9: \n")
# Split user_inputed numbers into individual numbers, store it in a list.
possible_numbers = user_input.strip().split(" ")
# We user list comprehensive to get rid of "for" loop, reduce code amount.
float_numbers = [float(x) for x in possible_numbers]
# absolute numbers
absolute_numbers = [abs(x) for x in float_numbers]
# rounded numbers, in "int" style
int_numbers = [int(round(x)) for x in float_numbers]

import math
# floored numbers
floored_numbers = [math.floor(x) for x in float_numbers]
# ceilled numbers
ceil_numbers = [math.ceil(x) for x in float_numbers]

# alright, lets try to print smartly about all the numbers we have
# use the function "dir()"
env_variables = dir()
for var in env_variables:
	if "_numbers" in var:
		print var, ":", eval(var)