import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

TWITTER_URL='http://api.twitter.com/1.1/friends/list.json'

ctx= ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode= ssl.CERT_NONE

while True:
    print('')
    acct= input('Enter Twitter Account:')
    if (len(acct)<1): break
    url= twurl.augment(TWITTER_URL,
                       {'screen_name': acct,'count': '5'})
    print('Retrieving', url)
    connection=urllib.request.urlopen(url,context=ctx)
    data= connection.read().decode()
    headers= dict(connection.getheaders())
    print('Remaining',headers['x-rate-limit-remaining'])
    js= json.loads(data)
    print(json.dumps(js,indent=2))

    for u in js['users']:
        print(u['screen_name'])
        s = u['status']['text']
        print('',s[:50])