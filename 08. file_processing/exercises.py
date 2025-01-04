# 1. On the side panel there's a bear.txt file. The 
# existing code opens that file in read mode.
# Below that code, please read the file content and 
# print out the content.
file = open('files/bear.txt')


# 2. Read the bear.txt file, and print out the first 
# 90 characters of its content.
with open('files/bear.txt') as bear:
    content = bear.read()
    
print(content[:90])

# 3. Define a function that gets a single string 
# character and a filepath as parameters and returns 
# the number of occurences of that character in 
# the file.
def found_times(character, file_name):
    with open(file_name) as file:
        content = file.read()
    
    return content.count(character)

character = 'b'
file_name = 'files/bear.txt'
    
print(f'The character "{character}" is {found_times(character, file_name)} times in file {file_name}')

# 4. Use Python to create a file with name file.txt 
# and write the text snail there.
with open('files/file.txt', 'w') as file:
    file.write('snail')

# 5. Create a first.txt file that contains the first 90 characters of bear.txt.
# Note that you should read the content of bear.txt with Python, 
# extract its first 90 characters with Python, and write those characters in 
# first.txt with Python.
def obtain_characters():
    with open('files/bear.txt') as bear:
        content = bear.read()
    
    return content[:90]

def write_file(characters):
    with open('files/first.txt', 'w') as file:
        file.write(characters)
        
write_file(obtain_characters())

# 6. Append the text of bear1.txt to bear2.txt. In other words, 
# bear2.txt should contain its text and the text of bear1.txt after that.
with open('files/bear1.txt') as bear:
    content = bear.read()

with open('files/bear2.txt', 'a') as bear2: # to read content add + after a
    bear2.write(content)
    # to see content
    # bear2.seek(0)
    # print(bear2.read())

# 7. The existing content of data.txt looks like this:
# 1.3, 1.5
# 2.3, 2.7
# 
# Use Python to modify the content of data.txt so that its content looks like below:
# 1.3, 1.5
# 2.3, 2.7
# 1.3, 1.5
# 2.3, 2.7
# 1.3, 1.5
# 2.3, 2.7
# So, you need to find a way to insert the existing content two more times.
with open('files/data.txt', 'a+') as file:
    file.seek(0)
    content = file.read()
    file.write(('\n' + content) * 2)