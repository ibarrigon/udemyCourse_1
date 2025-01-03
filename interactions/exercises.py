# 1. Implement a function that gets a person's name as a parameter and 
# greets the person with Hi Person. For example, if I called your function 
# using foo("Marry") the function should return Hi Marry .
def salutation(name):
    return f'Hi {name}'

print(salutation('Angel'))

# 2. Implement a function that gets a person's name (e.g. john) as a
# parameter and returns a greeting (e.g. Hi John). Note that the first 
# letter of the person's name should always be uppercase.
def salutation(name):
    return f'Hi {name.capitalize()}'

print(salutation('jonh'))
