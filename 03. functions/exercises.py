# 1. Define a function that calculates the area of a square. For example, if I was to call your function with foo(7) 
# the output would be 49. If I called it with foo(3)  it would return 9, and so on. Note that you don't have to name 
# your function foo. Give it any name you want.
def square_area(side):
    return side * side

print(square_area(7), square_area(3))

# 2. Define a function that converts fluid ounces to milliliters knowing that 1 fluid ounce is equal to 29.57353 
# milliliters. For example, I was to call your function with foo(1) I would get an output of 29.57353. If I called it 
# with  foo(5) I would get 147.86765, and so on.
def volume_converter(ounces):
    return ounces * 29.57353

print(volume_converter(1), volume_converter(5))

# 3. Define a function that:
# (1) takes a temperature as a parameter
# (2) returns "Warm" if the temperature is greater than 7
# (3) returns "Cold" if the temperature is equal to or less than 7
# 
# If I called your function with foo(10) it would return Warm. If I called it with foo(7) or foo(5) it would return 
# Cold in both cases, and so on.
def check_temperature(temperature):
    if temperature > 7:
        return 'Warm'
    else:
        return 'Cold'

print(check_temperature(3), check_temperature(8))

# 4. Define a function that:
# (1) takes a string as a parameter
# (2) returns False if the string contains less than 8 characters
# (3) returns True if the string contains 8 or more characters
# 
# In other words, if I called your function with foo("mypass") it would return False. If I called it with 
# foo("mylongpassword") it would return True, and so on.
def check_password(password):
    return len(password) >= 8
    
print(check_password('my_pass'), check_password('aserejedejadejebere'))

# 4. Define a function that:
# (1) takes a temperature as a parameter
# (2) returns "Hot" if the temperature is greater than 25
# (3) returns "Warm" if the temperature is between 15 and 25, including 15 and 25.
# (4) returns "Cold" if the temperature is less than 15.
#
# If I called your function with foo(10) it would return "Cold". foo(15) or foo(16) or foo(25) would all 
# return "Warm" and foo(26) would return "Hot".
def check_temperature(temperature):
    if temperature > 25:
        return 'Hot'
    
    if temperature < 15:
        return 'Cold'
    
    return 'Warm'

print(check_temperature(10), check_temperature(16), check_temperature(26))