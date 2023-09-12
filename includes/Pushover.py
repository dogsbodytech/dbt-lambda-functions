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
		print(f'Error: Pushover failed with following params:\n{token},\n{user_key},\n{message},\n{priority}')
		return False
	return True

