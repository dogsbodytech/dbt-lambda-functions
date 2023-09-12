import json
from urllib.parse import unquote

from Pushover import send_pushover
from AWS_ParameterStore import get_ssm_parameter

ticket_url = "https://support.dogsbody.com/staff/tickets/"

def lambda_handler(event, context):
    # Sanitise input
    if 'ticket' not in event:
        return(json.dumps({'Message': 'Invalid data'}))

    try:
        ticket_data = json.loads(unquote(event['ticket']))
    except:
	# Input is already in JSON format
        ticket_data = event['ticket']

    # Sirportly sends two requests, one with no valid user.
    if ticket_data['user'] == None:
        return(json.dumps({'Message': 'Invalid data'}))

    user_data = ticket_data['user']
    user = user_data['username']
    subject = ticket_data['subject'].replace('+', ' ')
    url = ticket_url + ticket_data['reference']

    message = f'Update on: {subject}, Ticket: {url}'

    sirportly_key = get_ssm_parameter('SirportlyKey')
    user_keys     = get_ssm_parameter('PushoverUsers', False)
    user_key      = json.loads(user_keys)[user]

    params = {'token': sirportly_key, 'user': user_key, 'message': message}

    # send_pushover(token: str, user_key: str, message: str, priority = 0: int)
    if send_pushover(sirportly_key, user_keys, message) == True:
        print('Pushover Sent!')
        return(json.dumps({'Message': 'Pushover sent'}))
    else:
        return(json.dumps({'Message': 'Pushover failed, check CloudWatch logs'}))

def main():
    print('Running locally...')
    print(lambda_handler('ticket=%7B%22id%22%3A343301%2C%22reference%22%3A%22AB-12345%22%2C%22subject%22%3A%22OK+-+CPU+Usage+%3E+80+on+ex2.example.net%22%2C%22message_id%22%3A%22a2066783-c602-483c-898d-e28fb6d73d9a%40support.example.com%22%2C%22submitted_at%22%3A%222023-09-11T17%3A57%3A53%2B01%3A00%22%2C%22updated_at%22%3A%222023-09-11T18%3A05%3A17%2B01%3A00%22%2C%22reply_due_at%22%3A%222023-09-12T11%3A00%3A00%2B01%3A00%22%2C%22resolution_due_at%22%3Anull%2C%22auth_code%22%3A%22KDTAJp8N1keX%22%2C%22last_update_posted_at%22%3A%222023-09-11T17%3A57%3A53%2B01%3A00%22%2C%22first_response_time%22%3Anull%2C%22first_resolution_time%22%3Anull%2C%22resolution_time%22%3Anull%2C%22last_respondant%22%3A%22contact%22%2C%22update_count%22%3A2%2C%22status%22%3A%7B%22id%22%3A9%2C%22name%22%3A%22Waiting+for+Triage%22%2C%22colour%22%3A%22F27800%22%2C%22position%22%3A2%2C%22status_type%22%3A0%7D%2C%22priority%22%3A%7B%22id%22%3A2%2C%22name%22%3A%22Urgent%22%2C%22colour%22%3A%22f80000%22%2C%22position%22%3A2%7D%2C%22department%22%3A%7B%22id%22%3A1%2C%22name%22%3A%22SysAdmin%22%2C%22brand%22%3A%7B%22id%22%3A1%2C%22name%22%3A%22Fun+Company%22%2C%22url%22%3A%22https%3A%2F%2Fwww.example.com%2F%22%2C%22phone%22%3A%22%2B44+%280%291276+123456%22%7D%2C%22private%22%3Afalse%7D%2C%22team%22%3A%7B%22id%22%3A1%2C%22name%22%3A%22All+Staff%22%7D%2C%22user%22%3A%7B%22id%22%3A2%2C%22username%22%3A%22danbenton%22%2C%22first_name%22%3A%22Dan%22%2C%22last_name%22%3A%22Benton%22%2C%22job_title%22%3A%22Director%22%2C%22avatar_url%22%3A%22https%3A%2F%2Fsecure.gravatar.com%2Favatar%2Faf47d766d230f29831f94c5195fb5824%3Frating%3DPG%26size%3D%7B%7Bsize%7D%7D%26d%3Dmm%22%7D%2C%22sla%22%3A%7B%22id%22%3A1%2C%22name%22%3A%22Default+-+2+hour+response+9-5%22%2C%22reply_in%22%3A120%2C%22resolution_in%22%3Anull%7D%2C%22contact%22%3A%7B%22id%22%3A3258%2C%22reference%22%3Anull%2C%22name%22%3A%22Minder%22%2C%22abbreviated_name%22%3A%22Minder%22%2C%22company%22%3A%22Fun+Company+Ltd.%22%2C%22mail_format%22%3A%22both%22%2C%22picture_url%22%3A%22https%3A%2F%2Fsecure.gravatar.com%2Favatar%2F2f1a566dc0d8f19abab087300ba2dd67%3Frating%3DPG%26size%3D90%26default%3Dblah%22%2C%22discussion_count%22%3A347%2C%22pin%22%3A%22%22%2C%22created_at%22%3A%222019-03-16T22%3A12%3A40%2B00%3A00%22%7D%2C%22contact_method%22%3A%7B%22id%22%3A3173%2C%22method_type%22%3A%22email%22%2C%22data%22%3A%22minder%40example.com%22%2C%22default%22%3Atrue%7D%2C%22additional_contact_methods%22%3A%5B%5D%2C%22original_ticket%22%3Anull%2C%22source%22%3A%7B%22id%22%3A4%2C%22address%22%3A%22sysadmin%40example.com%22%2C%22name%22%3A%22Fun+Company+Ltd.%22%2C%22allow_outbound%22%3Atrue%2C%22subject_prefix%22%3A%22%22%2C%22send_as_user%22%3Atrue%2C%22test_enabled%22%3Atrue%2C%22type%22%3A%22IncomingAddress%22%7D%2C%22tags%22%3A%5B%5D%2C%22linked_tickets%22%3A%5B%5D%7D',''))

if __name__ == "__main__":
    main()

