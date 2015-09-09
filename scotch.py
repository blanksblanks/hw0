import csv

infile = open("iowa-liquor-sample.csv")
spamreader = csv.reader(infile, delimiter=',')
sum = 0 
for row in spamreader:
    for entry in row:
        if "single malt scotch" in entry.lower():
            sum += 1
            break
print sum

