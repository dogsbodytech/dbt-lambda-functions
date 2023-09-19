# Initial Configuration / Requirements
These steps should only need to be done once and by hand.

They are mainly here as a form of documentation of what was done

## S3 Bucket for Terraform state
We don't create this via Terraform as if someone does a `terraform destroy` then we will lose all state and history.

Create an S3 bucket called 'dogsbody-terraform-state' in 'eu-west-2' and *enable versioning*

## Create two policies
dbt-lambda-functions-deploy
dbt-lambda-functions-runtime


## Create a Deploy User
Create a user in IAM called 'dbt-lambda-functions-deploy'
Assign the policy dbt-lambda-functions-deploy

## Create the Runtime role
Create a role dbt-lambda-functions-runtime
Assign the policy dbt-lambda-functions-runtime


## Create an API Gateway






