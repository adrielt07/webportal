terraform {
  backend "s3" {
    bucket         = "web-portal-terraform-tfstate" # must be unique. Change this to match with your AWS bucket
    key            = "web_portal.tfstate"
    region         = "us-west-1"
    encrypt        = true
    dynamodb_table = "web-portal-terraform-state-lock"
  }
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

provider "aws" {
  region = "us-west-1"
}

locals {
  prefix = "${var.prefix}-${terraform.workspace}"
  common_tags = {
    Environment = terraform.workspace
    Project     = var.project
    Owner       = var.contact
    ManagedBy   = "Terraform"
  }
}


data "aws_region" "current" {}
