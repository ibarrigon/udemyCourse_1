print([i*2 for i in [1, 5, 10]]) # Output: [2, 10, 20]

print([i*2 for i in [1, -2, 10] if i>0])  # Output: [2, 20]

print([i*2 if i>0 else 0 for i in [1, -2, 10]]) # Output: [2, 0, 20]