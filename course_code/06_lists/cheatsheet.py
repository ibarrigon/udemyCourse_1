# A list comprehension is an expression that creates a list by iterating over another container.
# 
# A basic list comprehension:

print([i * 2 for i in [1, 5, 10]]) # Output: [2, 10, 20]

# List comprehension with if condition:
print([i * 2 for i in [1, -2, 10] if i > 0]) # Output: [2, 20]

# List comprehension with an if and else condition:
print([i * 2 if i > 0 else 0 for i in [1, -2, 10]]) # Output: [2, 0, 20]