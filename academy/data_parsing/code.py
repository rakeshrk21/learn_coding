import csv

outfile = open("onlytenants", "w")
with open("/Users/rakeshra/Developer/PerfDev/learn_python/data_parsing/homepage.csv", 'r') as infile:
    reader = csv.reader(infile, delimiter=',')
    for row in reader:
        tenandId = row[11]
        outfile.write(tenandId)
        outfile.write('\n')
    
outfile.close()
        
    
    
