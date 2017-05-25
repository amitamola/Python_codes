fname= raw_input("Enter the file name:")
op= open(fname)
count= dict()
for m in op:
    if m.startswith("From "):
       p=m.split()
       k=p[5]
       j=k.split(':')
       if j[0] in count:
          count[j[0]]=count[j[0]]+1
       else:
          count[j[0]]=1
          
l= sorted([(a,b) for a,b in count.items()])
for h,i in l:
  print h,i