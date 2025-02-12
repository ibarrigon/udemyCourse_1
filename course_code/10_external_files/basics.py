import pandas
 
data_frame_1 = pandas.DataFrame([2, 4, 6], [10, 20, 30])
print(data_frame_1)
#    0  1  2
# 1  2  4  6
# 2 10 20 30

data_frame_2 = pandas.DataFrame([2, 4, 6], [10, 20, 30], columns = ['Price', 'Age', 'Value'])
print(data_frame_2)
#    Price Age Value
# 1      2   4     6
# 2     10  20    30

data_frame_3 = pandas.DataFrame([2, 4, 56], [10, 20, 30], columns = ['Price', 'Age', 'Value'], index = ['First', 'Second'])
print(data_frame_3)
#        Price Age Value
# First      2   4     6
# Second    10  20    30

data_frame_4 = pandas.DataFrame({'Name': 'Jack'}, {'Name': 'Jonh'})
print(data_frame_4)
#   Name
# 0 Jack
# 1 Jonh

data_frame_5 = pandas.DataFrame({'Name': 'Jack', 'Surname': 'Jackie'}, {'Name': 'Jonh'})
print(data_frame_5)
#   Name Surname
# 0 Jack  Jackie
# 1 Jonh     NaN

print(data_frame_2.mean())
# Price     6.0
# Age      12.0
# Value    18.0
# dtype: float64

print(data_frame_2.mean().mean())
# 12.0

print(data_frame_3.Price)
# First      2
# Second    10
# Name: Price, dtype: int64

print(data_frame_3.Price.mean())
# 6.0

print(data_frame_3.Price.max())
# 10