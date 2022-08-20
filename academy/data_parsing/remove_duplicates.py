line_read = set()
outfile = open("outfile", 'w')
for line in open("/Users/rakeshra/Developer/PerfDev/learn_python/data_parsing/moretenants", "r"):
    if line not in line_read:
        outfile.write(line)
        line_read.add(line)
outfile.close()
        