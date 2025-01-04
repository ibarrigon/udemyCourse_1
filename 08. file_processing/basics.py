# open a file
myfile = open('files/fruits.txt') # goes to ram
print(myfile.read()) # show the file and moves the point goes to the end of file
print(myfile.read()) # show blank line
myfile.close() # not mandatory but recommended. needs to do after read.

# alternative method
opened_file = open('files/fruits.txt')
content = opened_file.read()
opened_file.close() # not mandatory but recommended

print(content.read()) # show the file and moves the point goes to the end of file
print(content.read()) # show blank line

# better way. using with. we don't need to close the file
with open('files/fruits.txt') as myfile_with:
    content = myfile_with.read()
    
print(content)

# other directory
with open('files/other_fruits.txt') as other_directory:
    content2 = other_directory.read()

print(content2)

# writing. second parameter is (by default) 'r' (read) for write process you need 'w'
with open('files/vegetables.txt', 'w') as vegetables: 
    vegetables.write('Tomato\nCucumber\nOnion')
    vegetables.write(' Garlic') # writes directly after 'Onion'. You need to use \n for new line

# if file don't exists, then its created, in other case, overwrite

# better way. write every vegetable in new line
with open('files/vegetables.txt', 'w') as vegetables: 
    vegetables.write('Tomato\nCucumber\nOnion\n')
    vegetables.write('Garlic')

# better way. line by line
with open('files/vegetables.txt', 'w') as vegetables: 
    vegetables.write('Tomato')
    vegetables.write('\nCucumber')
    vegetables.write('\nOnion')
    vegetables.write('\nGarlic')

with open('files/vegetables.txt', 'a') as vegetables: 
    vegetables.write('\nOkra')
    # can't use .read()

with open('files/vegetables.txt', 'a+') as vegetables: 
    vegetables.write('\nanother')
    vegetables.seek(0) # reset pointer
    content = vegetables.read()

print(content) # Output: all the file
