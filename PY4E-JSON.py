import urllib.request, urllib.parse, urllib.error
import json
import ssl


# sample address 
# http://py4e-data.dr-chuck.net/comments_42.json
# actual address
# http://py4e-data.dr-chuck.net/comments_678088.json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter location: ')


uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
js = str(data)


a = js.find('[')
b = js.find(']')


info = json.loads(js[a:b+1])
k = 0
for item in info:
	k = k + item['count']
	
print(k)