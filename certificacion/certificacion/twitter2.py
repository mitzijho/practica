import urllib.request, urllib.parse, urllib.error
from twurl import augment
import ssl

print('*Calling Twitter...')
url= augment('http://api.twitter.com/1.1/statuses/user_timeline.json',
             {'screen_name':'drchuck','count':'2'})

print(url)

ctx= ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode= ssl.CERT_NONE

Connection= urllib.request.urlopen(url, context=ctx)
data = Connection.read()
print(data)

print('===============================')
headers= dict(Connection.getheaders())
print(headers)