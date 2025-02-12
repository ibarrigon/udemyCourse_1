import pandas

data_csv_1 = pandas.read_csv('files/supermarket-commas.txt')

data_csv_1 = pandas.read_csv('files/supermarket-semi-commas.txt', sep=';')