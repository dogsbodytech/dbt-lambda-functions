import json
import boto3
from urllib import unquote

from Pushover import get_pushover_user_key, send_pushover

# Fetch Sirportly key
ssm = boto3.client('ssm')
sirportly_key = ssm.get_parameter(Name='SirportlyKey',WithDecryption=True)['Parameter']['Value']

def lambda_handler(event, context):
	# Sanitise input
	if 'ticket' not in event:
		return(json.dumps({'Message': 'Invalid data'}))

	ticket_data = json.loads(unquote(event['ticket']))

	# Sirportly sends two requests, one with no valid user.
	if ticket_data['user'] == None:
		return(json.dumps({'Message': 'Invalid data'}))

	user_data = ticket_data['user']
	user = user_data['username']
	subject = ticket_data['subject'].replace('+', ' ')
	url = ticket_url + ticket_data['reference']

	message = f'Update on: {subject}, Ticket: {url}'

	params = {'token': sirportly_key, 'user': get_pushover_user_key(user), 'message': message}

	# send_pushover(token: str, user_key: str, message: str, priority = 0: int)
	if send_pushover(sirportly_key, user_keys, message) == True:
		print('Pushover Sent!')
		return(json.dumps({'Message': 'Pushover sent'}))
	else:
		return(json.dumps({'Message': 'Pushover failed, check CloudWatch logs'}))
