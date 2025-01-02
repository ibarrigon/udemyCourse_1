# combine two list, delete duplicates and sorted items

list1 = [5, 3, 8, 6, 3]
list2 = [7, 2, 5, 9, 8]

combined_list = list(set(list1 + list2))

combined_list.sort()

print(combined_list)