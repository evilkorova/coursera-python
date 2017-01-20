# Chapter 12 ex 3

import urllib.request, urllib.parse, urllib.error

url = input('Enter a URL: ')

try:
    page = urllib.request.urlopen(url).read()
except:
    print('Error in connecting to %s' % url)
    quit()

print(page[:3001])
print('Character count:' + str(len(page)))
