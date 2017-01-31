# Course 3, Week 4, Assignment 2

import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup

def PageSeq(url, c, pos):
    while c > 0:
        print('Retreiving: ' + url)
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        links = []
        for tag in tags:
            links.append(tag.get('href', None))
        url = links[pos-1]
        c -= 1
    return(url)

last = PageSeq('http://python-data.dr-chuck.net/known_by_Joss.html', 7, 18)
name = re.findall('known_by_(.+)\.html', last)

print('\nAnswer is: ' + name[0])
