def construct_phrase(text):
    interrogatives = ('how', 'what', 'why')
    
    output = text.capitalize()
    if text.lower().startswith(interrogatives):
        return '{}?'.format(output)
    
    return '{}.'.format(output)


inputs = []

while True:
    something = input('Say something: ')
    if something == '\end':
        break
    
    inputs.append(construct_phrase(something))
    

print(str.join(' ', inputs))
# we can use ' '.join(inputs)
