# 1. Append the value of current to the end of the list 
# seconds Please use the list.append() method to do that.
seconds = [1.23, 1.45, 1.02]
current = 1.11

seconds.append(current)

# 2. Remove item 1.45 from seconds.
seconds = [1.23, 1.45, 1.02, 1.11]
seconds.remove(1.45)
print(seconds)

# 3. Remove items 1.45, 1.02, and 1.11 from seconds.
seconds = [1.23, 1.45, 1.02, 1.11]

seconds.remove(1.45)
seconds.remove(1.02)
seconds.remove(1.11)

#  4. Complete the script so that it prints out the 3rd 
# item of list serials.
serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
print(serials[2])

# 5. Complete the script so that it prints out the 1st, 3rd, 
# and the 6th items of the list serials.
serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
print(serials[0], serials[2], serials[5])

# 6. Append the first item of weekend to workdays.
workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekend = ["Sat", "Sun"]

workdays.append(weekend[0])

# 7. Print out the slice ['b', 'c', 'd'] of the letters 
# list using slicing.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[1:4])

# 8. Print out the slice ['a', 'b', 'c'] of the letters 
# list using slicing.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[0:3])

# 9. Print out the slice ['e', 'f', 'g'] of the letters
# list using slicing.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[-3:])