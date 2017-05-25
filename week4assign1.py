fname = raw_input("Enter file name: ")
fh = open(fname)
b=list()
m=0
def checkrep(b,n):
    for q in range(len(n)):
         if n[q] in b:
            continue
         else:
            b.append(n[q])

for m in fh:
    n=m.split()
    checkrep(b,n)

b.sort()
print b