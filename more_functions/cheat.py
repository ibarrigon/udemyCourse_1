#1
def volume(a, b, c):
    return a * b * c

# 2 
def converter(feet, coefficient = 3.2808):
    meters = feet / coefficient
    return meters
 
print(converter(10)) # Output: 3.0480370641306997

# 3
print(volume(1, b = 2, c =1))

# 4
def find_max(*args):
    return max(args)
print(find_max(3, 99, 1001, 2, 8)) # Output: 1001

# 5
def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get)
 
print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34)) # Output: Sim

