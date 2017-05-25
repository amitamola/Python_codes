import urllib
import json

url1 = 'http://python-data.dr-chuck.net/comments_312814.json'
htm1= urllib.urlopen(url1).read()

info = json.loads(htm1)
print 'User count:', len(info)
m=0
k=0
for item in info["comments"]:
    m=m+(int)(info["comments"][k]["count"])
    k+=1
print m