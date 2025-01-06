import pandas
 
df1 = pandas.DataFrame([2, 4, 6], [10, 20, 30])
print(df1)
#    0  1  2
# 1  2  4  6
# 2 10 20 30

df2 = pandas.DataFrame([2, 4, 6], [10, 20, 30], columns = ['Price', 'Age', 'Value'])
print(df2)
#    Price Age Value
# 1      2   4     6
# 2     10  20    30

df3 = pandas.DataFrame([2, 4, 56], [10, 20, 30], columns = ['Price', 'Age', 'Value'], index = ['First', 'Second'])
print(df3)
#        Price Age Value
# First      2   4     6
# Second    10  20    30

df4 = pandas.DataFrame({'Name': 'Jack'}, {'Name': 'Jonh'})
print(df4)
#   Name
# 0 Jack
# 1 Jonh

df5 = pandas.DataFrame({'Name': 'Jack', 'Surname': 'Jackie'}, {'Name': 'Jonh'})
print(df5)
#   Name Surname
# 0 Jack  Jackie
# 1 Jonh     NaN

print(df2.mean())
# Price     6.0
# Age      12.0
# Value    18.0
# dtype: float64

print(df2.mean().mean())
# 12.0

print(df3.Price)
# First      2
# Second    10
# Name: Price, dtype: int64

print(df3.Price.mean())
# 6.0

print(df3.Price.max())
# 10