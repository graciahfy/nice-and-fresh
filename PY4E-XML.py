import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter - ')
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
    
stuff = ET.fromstring(data)
lst = stuff.findall('comments/comment')
print('User count:', len(lst))

a = 0
for item in lst:
    b = item.find('count').text
    c = int(b)
    a = a + c
    
print("Sum: ", a)