# Library and functions to interact with the Pushover API
# Details of the API can be found at https://pushover.net/api#messages

import http.client
import urllib
import boto3

ssm = boto3.client('ssm')

def get_pushover_user_key(username: str) -> str:
	"""
	Fetch pushover user key from SSM Parameter Store.
	"""
	user_keys = ssm.get_parameter(Name='PushoverUsers',WithDecryption=False)['Parameter']['Value']
	return json.loads(user_keys)[user]

def send_pushover(token: str, user_key: str, message: str, priority: int = 0) -> bool:
	"""
	Send pushover _message_ to _user_.

	Output: True if successful, else False
	"""
	try:
		# Open connection
		with http.client.HTTPSConnection("api.pushover.net:443") as conn:
			conn.request("POST", "/1/messages.json",
			urllib.parse.urlencode({
				"token": token,
				"user": user_key,
				"message": message,
				"priority": priority
			}), { "Content-type": "application/x-www-form-urlencoded" })
			result = conn.getresponse()
		# Confirm success
		assert result.code == 200
	except:
		print('Error occured sending pushover with the following params:')
		print(f'message: {message}')
		return False
	return True

