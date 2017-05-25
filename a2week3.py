file=raw_input("Enter file name:")
two=open(file)
index= None
k=0
count=0

for line in two:
    line=line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
         index=line.find('0')
         m=line[index:len(line)]
         n=float(m)
         k=k+n
         count+=1

print "Average spam confidence: ",k/count