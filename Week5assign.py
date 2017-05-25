m=0
largest=None
smallest=None
while(m==0):
    value=raw_input("Enter the number or type done to finish:")
    try:
      val=int(value)
      if largest==None:
        largest= val
      if largest<val:
        largest=val
      if smallest==None:
        smallest= val
      if smallest>val:
        smallest=val
        
     
    except:
        if(value=="done"):
            m=1
            break
            
        else:
            print "Invalid input"
        
print "Maximum is ",largest
print "Minimum is ",smallest