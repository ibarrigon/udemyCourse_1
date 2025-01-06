# In  the previous lecture, you learned that you can load a CSV file with this code:
#
# import pandas
# df1 = pandas.read_csv("supermarkets.csv")
# Try loading the supermarkets.json file for this exercise using read_json instead of read_csv.
#
# The supermarkets.json file can be found inside the supermarkets.zip file attached in the previous lecture.
import pandas

file = pandas.read_json('./files/supermarket.json')