# Allows the user to input a list of words in the terminal and let them specify the minimum word
#
# Output:
# Enter a list of words separated by spaces: bottle cup sand
#
# Identifies the longest word(s) in the list, including multiple words with the same maximum length and 
# prints out a message that includes the number of characters of that word:
#
# Output:
# The longest word(s) with 6 charaters:
#   - bottle

def longest_words(words):
    longest_words_list = []
    word_length = 0
    
    for word in words: 
        current_length = len(word)
        if current_length > word_length:
            longest_words_list.clear()
            word_length = len(word)
        
        if current_length == word_length:
            longest_words_list.append(word)
    
    return {'word_length': word_length, 'words': longest_words_list}

words = input('Enter a list of words separated by spaces: ')
words_list = words.split(' ')

result = longest_words(words_list)

print(f"The longest word(s) with {result['word_length']} characters")
for word in result['words']:
    print(f'- {word}')