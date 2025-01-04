# 1. Implements a function that takes two strings 
# as parameters, concatenates them, and returns 
# the result.
def concatenate_strings(string1, string2):
    return string1 + string2

print(concatenate_strings('asereje', 'deje'))

# 2. Define a function that takes an indefinite number of 
# numbers as arguments and returns their average. If I called 
# your function with foo(10, 20, 30, 40) it should return the 
# 25, the average of those numbers.
def average(*args):
    return sum(args) / len(args)

print(average(10, 20, 30, 40)) # Output: 25.0

# 3. Define a function that takes an indefinite number of 
# strings as parameters and returns a list containing all 
# the strings in UPPERCASE and sorted alphabetically. For 
# example, if I called your function with 
# foo("snow", "glacier", "iceberg") it should 
# return ["GLACIER", "ICEBERG", "SNOW"].
def sort_alphabetic(*args):
    sorted = list(text.upper() for text in args)
    sorted.sort()
    
    return sorted

print(sort_alphabetic("snow", "glacier", "iceberg"))

# 4. Enter the correct parameters inside find_sum() so that 
# the output of the code is 9.
def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(a = 1, b = 3, c = 2, d = 3))