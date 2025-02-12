import pandas

f = pandas.read_csv('files/supermarkets.csv')

# add info
data_txt = pandas.read_csv('files/data.txt', header = None) # the file has no header (columns name)
data_txt.columns = ['ID', 'Address', 'City', 'State', 'Country', 'Name', 'Employees']

# change index
data_txt_2 = data_txt.set_index("ID") # Column ID is the index. This don't modify data_txt
data_txt_3 = data_txt.set_index("ID", inplace = True) # Column ID is the index. data_txt it's modified
data_txt_4 = data_txt.set_index("Address", inplace = True) # Column Address is the index. data_txt it's modified
data_txt_5 = data_txt.set_index("Name", inplace = True, drop = False) # Column ID is the index. data_txt it's modified. Column its not removed

# filter
data_txt_1 = pandas.read_csv('files/data.txt', header = None) # the file has no header (columns name)
data_txt_1.columns = ['ID', 'Address', 'City', 'State', 'Country', 'Name', 'Employees']

print(data_txt_1.loc['1':'3', 'Country': 'ID'])
print(data_txt_1.loc[:, 'Country'])
print(data_txt_1.iloc[1:3, 1:3])
print(data_txt_1.iloc[:, 1:4])
print(data_txt_1.iloc[:, 1])

# access cell
print(data_txt_1.ix[1:4])

# delete
print(data_txt_1.drop['3']) # don't change data frame

print(data_txt_1.drop(data_txt.index[1:3])) # delete rows
print(data_txt_1.drop(data_txt.columns[1:3])) # delete columns

# data_txt_1['Continent'] = ['North America'] -> error, you need to put exact number of index
data_txt_1['Continent'] = ['North America', 'North America', 'North America', 'North America', 'North America']
data_txt_1['Continent'] = data_txt_1.shape[0] * ['North America']

print(data_txt_1.shape) # Output (5, 8) (<rows>, <columns>)

data_txt_1['Continent'] = data_txt_1['Country'] + ', North America' # change value

# Add row
# Trick: Transpose data frame, add column and transpose again
data_txt_1_t = data_txt_1.T # transposed data frame
