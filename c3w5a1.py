# Course 3 Week 5 Assignment 1

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_306616.xml'

print('Retreiving', url)
data = urllib.request.urlopen(url).read()

print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
counts = tree.findall('.//count')
print('Count:', len(counts))

lst = []

for i in counts:
    lst.append(int(i.text))

print('Sum:', sum(lst))
