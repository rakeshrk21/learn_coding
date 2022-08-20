import csv

with open("/Users/rakeshra/Developer/PerfDev/learn_python/data_parsing/onlytenants", 'r') as infile:
    reader = csv.reader(infile)
    for line in reader:
        print(line[0])

            

    
    