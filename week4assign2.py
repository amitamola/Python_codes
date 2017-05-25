import re
import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')

list1=list()

for i in range (7):
    htm1= urllib.urlopen(url).read()
    soup1=BeautifulSoup(htm1)
    tags1= soup1('a')
    for tag1 in tags1:
        x2 = tag1.get('href', None)
        list1.append(x2)
    
    y= list1[17]
    if len(x2) < 18:
        print "Incomplete data"
        break
    else:
        url=y             
    print y
    list1[:]=[]