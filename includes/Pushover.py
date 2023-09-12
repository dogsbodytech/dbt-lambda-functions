# Library and functions to interact with the Pushover API
# Details of the API can be found at https://pushover.net/api#messages

import http.client
import urllib

def send_pushover(token: str, user_key: str, message: str, priority: int = 0) -> bool:
	"""
	Send pushover _message_ to _user_.

	Output: True if successful, else False
	"""
	try:
		# Open connection
		conn = http.client.HTTPSConnection("api.pushover.net:443")
		conn.request("POST", "/1/messages.json",
		urllib.parse.urlencode({
			"token": token,
			"user": user_key,
			"message": message,
			"priority": priority
		}), { "Content-type": "application/x-www-form-urlencoded" })
		result = conn.getresponse()
		conn.close()
		# Confirm success
		assert result.code == 200
	except Exception as err:
		print(f'Error: Pushover failed with following params:\n{token},\n{user_key},\n{message},\n{priority}')
		print(f'Error: Response {err}')
		return False
	return True

