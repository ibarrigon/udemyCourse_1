def mean(my_list):
    the_mean = sum(my_list) / len(my_list)
    return the_mean

def mean_extended(my_list):
    if isinstance(my_list, dict):
        value = my_list.values()
    else:
        value = my_list
    the_mean = sum(value) / len(value)
    return the_mean

print(mean([1, 4, 6, 7, 3, 2]))

print(mean_extended([1, 4, 6, 7, 3, 2]), mean_extended({'Jorge': 10.0, 'Maria': 5.6, 'Ana': 8.7}))
    