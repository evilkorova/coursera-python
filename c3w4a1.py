# Course 3, Week 4, Assignment 1

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'http://python-data.dr-chuck.net/comments_306619.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
numlist = []
for tag in tags:
    numlist.append((int(tag.contents[0])))

print (sum(numlist))
