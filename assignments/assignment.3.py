infile = open("/home/ramesh/Documents/Ramesh.assigment.txt","r")
# note: I have rewrittent the code to iterate using a for loop instead of a while loop; it's much simpler that way!
aline = infile.readline()
#while aline:
for aline in infile:
    items = aline.split()
    dataline = items[0] + ','
    print(dataline)
    aline = infile.readline()
infile.close()