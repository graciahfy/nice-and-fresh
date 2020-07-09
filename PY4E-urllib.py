# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL ')



# repeat 4 times 
co = input('Enter count: ')
count = int(co)
b = 0
# position 3, start from 1 
po = input('Enter position: ')
pos = int(po)



while b < count: 
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	a = tags[pos - 1]
	url = a.get('href', None)
	print('Retrieving:', url)
	b += 1