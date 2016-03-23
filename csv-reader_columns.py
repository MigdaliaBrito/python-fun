#Objective: Compare 2 CSV files and output number of COLUMNS
#           that are a match

import csv #import csv utility

test1 = csv.reader(open('testdata1.csv'), delimiter=",")
test2 = csv.reader(open('testdata2.csv'), delimiter=",")

ncolsTest1 = len(next(test1))
ncolsTest2 = len(next(test2))
maxColumns = ncolsTest2
counter = 0

for n,o in zip(test1, test2):
    if n[0] == o[0]:
        print n, o , "MATCH ELEMENT 0"
    if n[1] == o[1]:
        print n, o , "MATCH ELEMENT 1"


#file end line
