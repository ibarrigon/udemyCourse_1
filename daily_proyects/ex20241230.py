# Write a program that takes a list of words and finds the longest word in that list. The program should also display the length of that word.
#
# Start by placing the following list in your script:
#
# words = ["apple", "banana", "cherry", "blueberry"]
#
# Output:
# "{blueberry}" is the longest word with 9 characters.

words = ["apple", "banana", "cherry", "blueberry"]

longest_word = ''

for word in words:
    if len(word) > len(longest_word):
        longest_word = word
    
print(f'"{longest_word}" is the longest word with {len(longest_word)} characters.')