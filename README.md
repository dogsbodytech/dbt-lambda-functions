# Dogsbody Technology Lambda Functions
This repo contains the Lambda functions used by Dogsbody Technology Ltd. 

Most of these functions act as simple webhooks to add aditional functionality that isn't offered natively.


## Repo
We have one repo for all Lambda functions. We did this for simplicity and to save duplication of code.

Each Lambda function exists in it's own subdirectory beginning `func_`

Shared (library) files are in the `includes` subdirectory. This folder is automatically included in each function.

### On commit
GitHub Actions do a thing....


## Lambda Functions

### func_Sirportly_Pushover
TBD

### func_Hello_World
A very basic "Hello World" function that can be used as a test/debug/template function


## Coding
We try not to use modules that are not part of the standard Python standard library (so far so good).

Some additional modules are included by AWS which can be used.

As of time of writing (Python 3.10 & 3.9) these are...
- awslambdaric
- boto3
- botocore
- jmespath
- pip
- python-dateutil
- s3transfer
- setuptools
- simplejson
- six
- urllib3


## To Do
- Get .github/workflows/main.yml building (and deploying) seperate functions when updated
  - Remember to use the branch name as part of the function name
- Re-write includes/Pushover.py for urllib3
- It would be great if we could store and control the individual Lambda functions in AWS. e.g. 
  - Allow us to control what runtime is used from this repo
  - Create the Lambda function in AWS if it doesn't exist
  - Connect the Lambda function to the API Gateway if not connected
- It would be great if we just deployed the fuctions that were updated (or all if the `includes` are)







