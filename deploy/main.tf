terraform {
  backend "s3" {
    bucket         = "ctrl-layer-web-portal-terraform-state"
    key            = "web_portal.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "ctrl-layer-web-portal-terraform-lock"
  }
}

provider "aws" {
  region = "us-east-1"
  version = "~> 2.50.0"
}
