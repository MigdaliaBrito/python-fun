#Objective: Compare 2 CSV files and output number of COLUMNS
#           that are a match

import csv #import csv utility

test1 = open('testdata1.csv', 'r')
test2 = open('testdata2.csv', 'r')

with open('testdata1.csv', 'r') as test1, open('testdata2.csv', 'r') as test2:
    reader1 = csv.reader(test1, delimiter=',', skipinitialspace=True)
    reader2 = csv.reader(test2, delimiter=',', skipinitialspace=True)


    #Lets count columns?

    #CSV1
    first_row_a = next(reader1)
    num_cols_a = len(first_row_a)

    #CSV2
    first_row_b = next(reader2)
    num_cols_b = len(first_row_b)



    #If cols do not share same # of cols
    while num_cols_a != num_cols_b:
        lowestNum = min(num_cols_a, num_cols_b)

        for i in range(lowestNum):
            for x in reader1:
                for y in reader2:
                    if x[i] == y[i]:
                        print x[i], y[i]

    
    for x in reader1:
        #print rows[0], rows[1] #column1, column2
        for y in reader2:
            if x[0] == y[0]:
                print "MATCH MATCH"
                print x[0], y[0]

            if x[1] == y[1]:
                print "MATCH MATCH 1"
                print x[1], y[1]


#Close files
test1.close()
test2.close()