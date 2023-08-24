import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello World!')
    }

def main():
    print('Running locally...')
    print(lambda_handler('',''))

if __name__ == "__main__":
    main()

