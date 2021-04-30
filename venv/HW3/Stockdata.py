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

import os
from urllib.request import urlopen

# current working directory
print(os.getcwd())

# Stock codes, entered as values in a dictionary, I will be downloading from Yahoo Finance.
codes = {'IPF','NPN','PRX','PAN','RNI','TCP','VOD'}

# link to yahoo historical data download, replaced stock code in link with string formating from the codes dictionary
# FYI it seems the link changes over time so we will have to amend the link if needs be
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
    # opening the in_file as read file and out_file as the write file
    with open(in_file + f + '.csv', 'r') as inf,\
            open(out_file + f + '.csv', 'w', newline ='') as outf:
        reader = inf.readlines() # reading each line from the in_file and defining it to reader
        # loop through each row of the in_file
        for row in reader:
            newline = row.strip('\n') # getting rid of the \n so I can add it to a list without it
            line= newline.split(',') # splitting by comma and creating a py list defined by line

            # Append Change to the row if the first element in line is "Date"
            if line[0] == 'Date' :
                line.append('Change')
                header = line

                # To avoid the trailing comma we loop through each element of the row, if it is the last element we do not write a comma.
                for x in header:
                    if x == header[-1]:
                        outf.write(str(x))
                    else:
                        outf.write(str(x) + ',')
                outf.write('\n')
             # if the first element in line is not "Date" then we append the algorithm result to the row
            else:
                change = (float(line[4]) - float(line[1])) / float(line[1])
                line.append(change)
                chg = line

                # To avoid the trailing comma we loop through each element of the row, if it is the last element we do not write a comma.
                for el in chg:
                    if el == chg[-1]:
                        outf.write(str(el))
                    else:
                        outf.write(str(el) + ',')
                outf.write('\n')










