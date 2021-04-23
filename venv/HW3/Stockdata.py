# Instructions
# 1. Please download a CSV file containing the stock history of some companies, for example from:
# http://finance.yahoo.com/q/hp?s=GOOG
# http://finance.yahoo.com/q/hp?s=IBM
# http://finance.yahoo.com/q/hp?s=MSFT
#
# (Download Data)
# Save files giving them different names to a local folder on your drive
#
# 2. Write a program that searches for CSV files with stock rates in a given folder and for every one of them:
#
# 3. Calculates the percentage change betweeen Close and Open price and adds these values as another column to this CSV file.
# You can replace the old file or create a new one.
#
# Change = (Close-Open)/Open
#
# 4. The output files can be stored in another folder
# 5. You can use Python to download files. An example is given here: https://github.com/prubach/Python_Summer_2021_2/blob/master/download_file.py
# 6. Please do not use pandas, or only use it as an alternative way of implementing it along a more "manual" way using just python without any libraries.

import csv
import os
from urllib.request import urlopen

# current working directory
# print(os.getcwd())

# Stock codes, entered as values in a dictionary, I will be downloading from Yahoo Finance.
codes = {'IPF','NPN','PRX','PAN','RNI','TCP','VOD'}

# link to yahoo historical data download, replaced stock code in link with string formating from the codes dictionary
url = 'https://query1.finance.yahoo.com/v7/finance/download/%s.JO?period1=1587622290&period2=1619158290&interval=1d&events=history&includeAdjustedClose=true'

for i in codes:
    urlt = url %i
    local_path = os.path.join('data', i + '.csv')
    with urlopen(urlt) as image, open(local_path, 'wb') as f:
        f.write(image.read())


# defining where to get the input date from and where to store the output data
in_file = os.path.join(os.getcwd() +'\Data\\')
out_file =os.path.join(os.getcwd() +'\output\\')


#running a loop to read and write the data as variables from codes dictionary
for f in codes:
    reader = csv.reader(open(in_file + f + '.csv', 'r')) #reading data from in_file
    writer = csv.writer(open(out_file + f + '.csv', 'w', newline=''))#writing the data to out_file
    for row in reader:
        if row[0] == 'Date' :
            row.append('Change')
            writer.writerow(row)
        else:
            row.append((float(row[4]) - float(row[1])) / float(row[1]))
            writer.writerow(row)











