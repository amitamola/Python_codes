import re
import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
count=0
g=0
tags = soup('span')
for tag in tags:
    k=str(tag)
    s=re.findall("[0-9]+",k)
    g=g+int(s[0])
    count+=1
print count
print g