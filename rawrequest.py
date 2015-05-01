__author__ = 'cweibel'

import requests, json

message = '[hello_rubble]'
URL_base = "https://rubble-beta.viditeck.com"
URL_rest = "/rubble/service/call?wrap-input-from=default&channel=pid(1403)"
URL = URL_base + URL_rest
try:
    post = requests.post(URL, data=message, auth=('uABY0Pf8htbo', 'zLXknuvGra4eNOMX'))
except Exception as e:
    print "There was an error connecting to the Rubble server", e
if post.status_code != 200:
    print "Unexpected HTTP status: %d" % post.status_code
data = json.loads(post.content)
print data

