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
  alias  = "main"
}

provider "aws" {
  region = "us-east-1"
  alias  = "useast1"
}

resource "aws_api_gateway_rest_api" "api" {
  name                         = "dbt-lambda-functions"
  description                  = "The Dogsbody Technology Lamdbda Functions"
  disable_execute_api_endpoint = true
  endpoint_configuration {
    types = ["EDGE"]
  }
}

resource "aws_acm_certificate" "cert" {
  provider          = aws.useast1
  domain_name       = "webhook03.dogsbody.com"
  validation_method = "DNS"
  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_api_gateway_domain_name" "domain" {
  domain_name     = "webhook03.dogsbody.com"
  certificate_arn = aws_acm_certificate.cert.id
  endpoint_configuration {
    types = ["EDGE"]
  }
}

resource "aws_api_gateway_base_path_mapping" "base_path_mapping" {
  api_id      = aws_api_gateway_rest_api.api.id
  domain_name = aws_api_gateway_domain_name.domain.domain_name
}


