#Objective: Compare 2 CSV files and output number of ROWS
#           that are a match

import csv #import csv utility

test1 = open('testdata1.csv', 'r')
test2 = open('testdata2.csv', 'r')
counter = 0

with open('testdata1.csv', 'r') as test1, open('testdata2.csv', 'r') as test2:
    reader1 = csv.reader(test1)
    reader2 = csv.reader(test2)

    for samerows in reader1:
        for samerowstwo in reader2:
            if samerows == samerowstwo:

                counter += 1

                if counter == 1:
                    print counter, " row match!"
                    print samerows, samerowstwo

                elif counter == 0:
                    print "No matching rows :("

                else:
                    print counter, " rows match!"
                    print samerows, samerowstwo


#Close files
test1.close()
test2.close()