import urllib
import xml.etree.ElementTree as ET

file= "http://python-data.dr-chuck.net/comments_312810.xml"
htm1= urllib.urlopen(file).read()
m=0

input=ET.fromstring(htm1)
lst=input.findall('comments/comment')
print "Count: ",len(lst)
for i in lst:
   num = i.find('count').text
   k=(int)(num)
   m=m+k
print m