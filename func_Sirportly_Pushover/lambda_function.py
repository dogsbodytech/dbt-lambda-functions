#import json
#from urllib import unquote
#from config import user_keys, sirportly_key
#from pushover import send_pushover
#
#def lambda_handler(event, context):
#    if 'ticket' in event:
#        ticket_data = json.loads(unquote(event['ticket']))
#        if ticket_data['user'] == None: # Sirportly sends two requests, one with no valid user.
#            return(json.dumps({'Message': 'Invalid data'}))
#        user_data = ticket_data['user']
#        user = user_data['username']
#        message = 'Update on: '+ticket_data['subject'].replace('+', ' ')+', Ticket: 'ticket_url+ticket_data['reference']
#        params = {'token': sirportly_key, 'user': user_keys[user], 'message': message}
#        if send_pushover(params) == True:
#            print('Pushover Sent!')
#            return(json.dumps({'Message': 'Pushover sent'}))
#        else:
#            return(json.dumps({'Message': 'Pushover failed, check CloudWatch logs'}))
#    else:
#        return(json.dumps({'Message': 'Invalid data'}))

