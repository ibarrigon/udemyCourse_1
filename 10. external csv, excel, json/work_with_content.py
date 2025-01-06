import pandas

f = pandas.read_csv('files/supermarkets.csv')

# add info
df = pandas.read_csv('files/data.txt', header = None) # the file has no header (columns name)
df.columns = ['ID', 'Address', 'City', 'State', 'Country', 'Name', 'Employees']

# change index
df2 = df.set_index("ID") # Column ID is the index. This don't modify df
df3 = df.set_index("ID", inplace = True) # Column ID is the index. df it's modified
df4 = df.set_index("Address", inplace = True) # Column Address is the index. df it's modified
df5 = df.set_index("Name", inplace = True, drop = False) # Column ID is the index. df it's modified. Column its not removed

# filter
df_1 = pandas.read_csv('files/data.txt', header = None) # the file has no header (columns name)
df_1.columns = ['ID', 'Address', 'City', 'State', 'Country', 'Name', 'Employees']

print(df_1.loc['1':'3', 'Country': 'ID'])
print(df_1.loc[:, 'Country'])
print(df_1.iloc[1:3, 1:3])
print(df_1.iloc[:, 1:4])
print(df_1.iloc[:, 1])

# access cell
print(df_1.ix[1:4])

# delete
print(df_1.drop['3']) # don't change data frame

print(df_1.drop(df.index[1:3])) # delete rows
print(df_1.drop(df.columns[1:3])) # delete columns

# df_1['Continent'] = ['North America'] -> error, you need to put exact number of index
df_1['Continent'] = ['North America', 'North America', 'North America', 'North America', 'North America']
df_1['Continent'] = df_1.shape[0] * ['North America']

print(df_1.shape) # Output (5, 8) (<rows>, <columns>)

df_1['Continent'] = df_1['Country'] + ', North America' # change value

# Add row
# Trick: Transpose data frame, add column and transpose again
df_1_t = df_1.T # transposed data frame
