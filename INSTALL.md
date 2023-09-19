# Initial Configuration / Requirements
These steps should only need to be done once and by hand.

They are mainly here as a form of documentation of what was done

Perhaps one day we'll automate these with Terraform but for now there is no need.

## S3 Bucket for Terraform state
We don't ever want to create this via Terraform as if someone does a `terraform destroy` then we will lose all state and history.

Create an S3 bucket called 'dogsbody-terraform-state' in 'eu-west-2' and *enable versioning*

## Create two policies
dbt-lambda-functions-deploy
dbt-lambda-functions-runtime


## Deploy Access

### Create Deploy Policy
Create an IAM policy called 'dbt-lambda-functions-deploy'
 {
     "Version": "2012-10-17",
     "Statement": [
         {
           "Effect": "Allow",
           "Action": "s3:ListBucket",
           "Resource": "arn:aws:s3:::dogsbody-terraform-state"
         },
         {
           "Effect": "Allow",
           "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
           "Resource": "arn:aws:s3:::dogsbody-terraform-state/dbt-lambda-functions.state"
         },
         {
             "Effect": "Allow",
             "Action": [
                 "iam:GetRole",
                 "iam:PassRole"
             ],
             "Resource": "arn:aws:iam:::role/dbt-lambda-functions-runtime"
         },
         {
             "Effect": "Allow",
             "Action": [
                 "lambda:CreateFunction",
                 "lambda:UpdateFunctionCode",
                 "lambda:GetFunction",
                 "lambda:UpdateFunctionConfiguration"
             ],
             "Resource": "arn:aws:lambda:eu-west-2::function:dlf-*"
         },
         {
             "Effect": "Allow",
             "Action": "s3:PutObject",
             "Resource": "arn:aws:lambda:eu-west-2::function:dlf-*"
         }
     ]
 }


### Create a Deploy User
Create a user called 'dbt-lambda-functions-deploy' and give it the 'dbt-lambda-functions-deploy' policy

Create an Access Key Pair and note down the details ;-) 

### GitHub Actions
Add three secrets to the GitHub repo as Repository secrets
- AWS_REGION = eu-west-2
- AWS_ACCESS_KEY_ID = <From_Deploy_User>
- AWS_SECRET_ACCESS_KEY = <From_Deploy_User>


## Create the Runtime role
Create a role dbt-lambda-functions-runtime
Assign the policy dbt-lambda-functions-runtime


## Create an API Gateway






