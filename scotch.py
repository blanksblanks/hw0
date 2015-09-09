import csv

input_file = open("iowa-liquor-sample.csv")
csv_file = csv.reader(input_file, delimiter=',')
num_whiskies = 0 
for row in csv_file:
    for entry in row:
        if "single malt scotch" in entry.lower():
            num_whiskies += 1
            break
print num_whiskies

