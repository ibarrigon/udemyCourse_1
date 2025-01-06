temps = [221, 234, 340, 230]

# 1. for loop
new_temps = []
for temp in temps:
    new_temps.append(temp / 10)
print(new_temps)

# 2. inline for
new_temps = [temp / 10 for temp in temps]
print(new_temps)

# 3. inline for with conditional
temps = [221, 234, 340, -9999, 230]
new_temps = [temp / 10 for temp in temps if temp != -9999]
print(new_temps)

# 4. inline for with conditional and else
temps = [221, 234, 340, -9999, 230]
new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]
print(new_temps)