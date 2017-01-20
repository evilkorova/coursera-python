# Chapter 12 ex 2

import socket

url = input('Enter a URL: ')

try:
    host = url.split('/')[2]
except:
    print('Not a valid URL')
    quit()

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mysock.connect((host, 80))
except:
    print('Error in connecting to %s' % url)
    quit()

cmd = 'GET %s HTTP/1.0\n\n' % url
mysock.send(cmd.encode())

page = ''
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    page += data.decode()
mysock.close()

print(page[:3001])
print('Character count:' + str(len(page)))
