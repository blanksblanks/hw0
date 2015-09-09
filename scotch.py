import csv

def file_reader(file_path):
    input_file = open(file_path)
    return csv.reader(input_file, delimiter=',')

def count_whiskey_apperance(csv):
    num_whiskies = 0 
    for row in csv:
        for entry in row:
            if "single malt scotch" in entry.lower():
                num_whiskies += 1
                break
    print num_whiskies

if __name__ == '__main__':
    csv = file_reader("iowa-liquor-sample.csv")
    count_whiskey_apperance(csv)
