import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

address = raw_input('Enter location: ')

url = serviceurl +'?'+ urllib.urlencode({'sensor':'false', 'address': address})
uh = urllib.urlopen(url)
data = uh.read()

js = json.loads(str(data))

print js["results"][0]["place_id"]

