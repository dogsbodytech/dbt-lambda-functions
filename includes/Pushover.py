
# This code needs to be re-written using urllib3 instead of requests

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

