# Lists are one of the most heavily used datatypes in Python. They are designed to store multiple other Python datatypes such as numbers, strings, and any other type. For today’s task, you need to process the following two lists:
# 
# list1 = [5, 3, 8, 6, 3]
# list2 = [7, 2, 5, 9, 8]
# Specifically, your task is to:
# 
# 1. Place the two lists in a .py file.
# 2. Add some code that combines the two lists into one single list.
# 3. Removes any duplicates from the combined list.
# 4. Sort the combined list in ascending order.
# 5. Print out the sorted list.
#
# output:
# [2, 3, 5, 6, 7, 8, 9]

list1 = [5, 3, 8, 6, 3]
list2 = [7, 2, 5, 9, 8]

combined_list = list(set(list1 + list2))

combined_list.sort()

print(combined_list)