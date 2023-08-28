
# This code needs to be re-written using either urllib or urllib3 instead of requests

# The old code was being passed one argument, 
# I think we should be passing multiple arguments this time
# At minimum then I think we use be passed...
#  - application key
#  - user/group key
#  - message
#  - priority (should default to 0/none if not set)
# ... this is based on the feilds we have used in the past
# We can add functionality like title and image attachments in the future if we need it.

# Details of the API can be found at https://pushover.net/api#messages


# This is the example that Pushover provide from
# https://support.pushover.net/i44-example-code-and-pushover-libraries#python
# 
#import http.client, urllib
#conn = http.client.HTTPSConnection("api.pushover.net:443")
#conn.request("POST", "/1/messages.json",
#  urllib.parse.urlencode({
#    "token": "APP_TOKEN",
#    "user": "USER_KEY",
#    "message": "hello world",
#  }), { "Content-type": "application/x-www-form-urlencoded" })
#conn.getresponse()


# This is the old code from our old Lambda function...
#
#import requests
#
#def send_pushover(params):
#    try:
#        r = requests.post('https://api.pushover.net/1/messages.json', params, timeout=30)
#        if r.status_code != requests.codes.ok:
#            raise requests.exceptions.RequestException
#        else:
#            return(True)
#    except requests.exceptions.RequestException:
#        print('Error occured sending pushover with the following params:')
#        print(params)
#        return(False)

