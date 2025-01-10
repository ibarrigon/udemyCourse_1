# 1. Loop over the colors items and print out the item in every loop. So, the expected output of your code would be:
# 11
# 34
# 98
# 43
# 45
# 54
# 54
colors = [11, 34, 98, 43, 45, 54, 54]
for color in colors:
    print(color)

# 2. Loop over the colors items and print out the item in every loop only if the item is greater than 50. So, the 
# output of your program would be:
# 98
# 54
# 54
colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:
    if color > 50:
        print(color)

# 3. Loop over the colors items and print out the item in every loop only if the item is an integer. So, the output 
# of your program would be:
# 11
# 43
# 54
# 54
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color in colors:
    if isinstance(color, int):
        print(color)
        
# 4. Loop over the colors items and print out the item in every loop only if the item is an integer and it is 
# greater than 50. So, the output of your program would be:
# 54
# 54
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color in colors:
    if isinstance(color, int) and color > 50:
        print(color)

# 5. Make the code print out the following output using a for loop:
# John Smith: +37682929928
# Marry Simpons: +423998200919
# 
# So, the code should loop over the dictionary items and in each iteration should print out the dictionary key, a 
# colon, a space, and the corresponding value.
dictionary = {'John Smith' : '+37682929928', 'Marry Simpons': '+423998200919'}

for agend in dictionary.items():
    print(f'{agend[0]}: {agend[1]}')
    
# 6. Loop over the phone_numbers values and in each loop print out the phone number, but with '00' instead of '+'. In 
# other words, your code should output:
# 0037682929928
# 00423998200919
#
# Hint: You can access dictionary values with phone_numbers.values() and you can replace characters 
# using str.replace().
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for phone in phone_numbers.values():
    print(phone.replace('+', '00'))

