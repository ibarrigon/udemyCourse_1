# 1. The program lets the user enter a directory path in the terminal where 
# some files are located (e.g., /Users/as/Downloads/myfolder for Mac/Linux or 
# C:\Users\as\Downloads\myfolder for Windows):
#
# Output:
# Enter the directory path to scan:
# 2. he program displays the list of the filepaths contained in the given directory 
# and their metadata (size, creation date, and type):
#
# Output:
# Metadata for all files:
# Path /Users/as/Downloads/myfolder/book.pdf, Size: 1119952 bytes, Created: 2024-12-27 
# 14:05:33, Modified: 2024-10-12 11:10:54, Type: .pdf
# ...
#
# 3. The program also lets the user choose whether to save the metadata results 
# in a CSV file or not:
#
# Output:
# Do you want to save the metadata to a CSV file? (y/n):
#
# Tip: You can extract the file creation time and size using the os library:
#
# Code:
# creation_time = os.path.getctime(file_path)
# modification_time = os.path.getmtime(file_path)
#
# Required Libraries: os, csv, datetime
import os
import pandas

directory = input('Enter the directory path to scan: ')
files = os.listdir(directory)

data = []
for file_name in files:
    creation_time = os.path.getctime(file_name)
    modification_time = os.path.getmtime(file_name)
    data.append({'file': file_name, 'creation': creation_time, 'modification': modification_time, 'size': '','type': ''})

while True:
    save = input('Do you want to save the metadata to a CSV file? (y/n):')
    if save == 'y' or save == 'n':
        break

if save == 'y':
    # save
    with open('.csv', 'w') as file:
        file.write(data)