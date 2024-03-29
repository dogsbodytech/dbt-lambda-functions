# Dogsbody Technology Lambda Functions
This repo contains the Lambda functions used by Dogsbody Technology Ltd. 

Most of these functions act as simple webhooks to add aditional functionality that isn't offered natively.


## Current Lambda Functions

### func_Sirportly_Pushover
TBD

### func_Hello_World
A very basic "Hello World" function that can be used as a test/debug/template function


## Repo
We have one repo for all Lambda functions. We did this for simplicity and to save duplication of code.

Each Lambda function exists in it's own subdirectory beginning `func_`

Shared (library) files are in the `includes` subdirectory. This folder is automatically included in each function. *Make sure filenames don't clash*.

### Branches
All development should be done in the `dev` branch ;-)

Once you have tested it (in AWS) then it can be moved to a production branch and re-deployed

### On commit
GitHub Actions deploy all the functions to AWS Lambda

The Lambda function will be created if it doesn't already exist

AWS Lambda functions are named `dlf-<branch>_<folder (minus func_)>` e.g. `dlf-dev_Hello_World`


## Initial Configuration / Requirements
These steps should only need to be done once and by hand so they can be found in [INSTALL.md](INSTALL.md)


## Create New Lambda Functions
- Create lambda_function.py in a new subfolder begining with `func_`
- When you are happy with your code add to the Matrix in /.github/workflows/main.yml
- When pushed to GitHub it should automatically create a Lambda Function in our AWS account
- You now need to go set it up in the API gateway...

### Coding
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
Phase One
- Document the creation of the API Gateway
- Document the creation of the Roles?
- Manually setup the "API Gateway" for "Hello_World" funtion
- Re-write includes/Pushover.py for urllib or urllib3
- Write func_Sirportly_Pushover/lambda_function.py :-p
- Manually setup the "API Gateway" for "Sirportly_Pushover" funtion
- Decide if we are using "v1" or "v3" for our production branch
- Create the production branch and setup manually in the AWS API Gateway

Phase Two
- GitHub Actions (.github/workflows/main.yml)
  - Somehow pull the Lambda Runtime from each function (and update it if it changes)
  - Iterate over all folders as opposed to using the matrix function
  - Connect the Lambda function to the API Gateway if not connected
  - It would be great if we just deployed the functions that were updated (or all if the `includes` are)

Phase Three
- Seperate IAM roles for each Lambda function that just gives it the AWS access that it needs

