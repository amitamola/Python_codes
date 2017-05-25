import re
fname= raw_input("Enter the file name:")
op= open(fname)
print op
s=0
h=0
for line in op:
    k=re.findall('[0-9]+',line)
    while s<len(k):
        q=int(k[s])
        h=h+q
        s+=1
    s=0
print h

