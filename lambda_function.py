
dogsbody_str = """
 ____                  _               _       
|  _ \  ___   __ _ ___| |__   ___   __| |_   _ 
| | | |/ _ \ / _` / __| '_ \ / _ \ / _` | | | |
| |_| | (_) | (_| \__ \ |_) | (_) | (_| | |_| |
|____/ \___/ \__, |___/_.__/ \___/ \__,_|\__, |
             |___/                       |___/ 
 _____         _                 _                   
|_   _|__  ___| |__  _ __   ___ | | ___   __ _ _   _ 
  | |/ _ \/ __| '_ \| '_ \ / _ \| |/ _ \ / _` | | | |
  | |  __/ (__| | | | | | | (_) | | (_) | (_| | |_| |
  |_|\___|\___|_| |_|_| |_|\___/|_|\___/ \__, |\__, |
                                         |___/ |___/ 
"""

def lambda_handler(event, context):
  return {
    'statusCode': 200,
    'body': dogsbody_str
  }
