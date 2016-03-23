#Objective: Compare 2 CSV files and output number of COLUMNS
#           that are a match

import csv #import csv utility

test1 = csv.reader(open('testdata1.csv'), delimiter=",")
test2 = csv.reader(open('testdata2.csv'), delimiter=",")
counter = 1

ncolsTest1 = len(next(test1))
ncolsTest2 = len(next(test2))
#test1.seek(0)
print ncolsTest1, ncolsTest2

#if ncolsTest1 == ncolsTest2

# for n in test1:
#     for l in test2:
#         if n[0] == l[0]:
#             print n[0], l[0]
#         else:
#             print counter, "jajajaja not a match ;)"
#         counter += 1
