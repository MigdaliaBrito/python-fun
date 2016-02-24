import csv
print "Helloww world."

with open('testdata1.csv', 'r') as test1:
    readTest1 = csv.reader(test1, delimiter=' ')
    for row in readTest1:
        print row