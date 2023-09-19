terraform {
  required_version = ">= 1.5.7"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.17.0"
    }
  }
  backend "s3" {
    bucket = "dogsbody-terraform-state"
    key    = "dbt-lambda-functions.state"
    region = "eu-west-2"
  }
}

provider "aws" {
  region = "eu-west-2"
}

