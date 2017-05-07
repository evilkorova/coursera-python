 # Week 6 assignment 1
# Extract data from json

import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter Location:')
if len(url) < 1:
    url = 'http://python-data.dr-chuck.net/comments_42.json'

print('Retrieving', url)

data = urllib.request.urlopen(url).read()

print('Retrieved', len(data), 'characters')
js = json.loads(data)

# Uncomment to see raw json in pretty format
#print(json.dumps(js, indent=4))

clist = []

for n in js['comments']:
    clist.append(int(n['count']))

print('Count:', len(clist))
print('Sum:', sum(clist))
