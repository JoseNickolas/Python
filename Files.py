fhandle = input("Enter file name:")
fhandle = open("mbox-short.txt","r")
count = 0
total = 0
average = 0
for line in fhandle:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    colpos = line.find(":")
    confpos = line.find("0")
    confnum = float(line[colpos+3:])
    count = count+1
    total = confnum+total
average = total/count
print("Average spam confidence:", average)
