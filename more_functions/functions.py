# multiple arguments
def area(a, b):
    return a * b

print(area(4, 5))

# multiple arguments. key argument
print(area(b=5, a=4))

# multiple arguments. key argument
print(area(a=4, b=5))

# multiple arguments. default value
def area2(a, b = 6):
    return a * b

print(area2(4))

# multiple arguments. default value key argument
print(area2(a = 4))

# multiple arguments. default value but different value
print(area2(4, 7))

# multiple arguments. default value key argument but different value
print(area2(a = 4, b = 7))

# default parameters must be latest arguments
# wrong: def area(a = 4, b):

# Arbitrary number of arguments. Can't no be keyword arguments
def mean_multiple_args(*args):
    return args

print(mean_multiple_args(1, 3, 'a, 4')) # Output (it's a tuple): (1, 3, 'a, 4')

def mean(*args):
    return sum(args) / len(args)

print(mean(1, 3, 4)) 

# Arbitrary number of arguments. Keyword arguments
def meankwords(*kwargs):
    return kwargs

# Error: print(mean(1, 3, 4)) 
print(mean(x = 1, y = 3, z = 4)) # Output (it's a dictionary): {'x': 1, 'y': 3, 'z': 4}