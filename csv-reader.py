#Objective: Compare 2 CSV files and output number of ROWS
#           that are a match

import csv #import csv utility

print "Helloww world."
test1 = open('testdata1.csv', 'r')
test2 = open('testdata2.csv', 'r')
counter

with open('testdata1.csv', 'r') as test1, open('testdata2.csv', 'r') as test2:
    reader1 = csv.reader(test1)
    reader2 = csv.reader(test2)

    for samerows in reader1:
        for samerowstwo in reader2:
            if samerows == samerowstwo:
                print samerows, samerowstwo
                print "Match!"
    # print list
    # #print out csv1
    # print "Test data 1"
    # for row in read1:
    #     print row
    #
    # #print out csv2
    # print "\nTest data 2"
    # for row in read2:
    #     print row


#Close these effing files, yo
test1.close()
test2.close()