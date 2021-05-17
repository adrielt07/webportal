terraform {
  backend "s3" {
    bucket         = "ctrl-layer-web-portal-terraform-state"
    key            = "web_portal.tfstate"
    region         = "us-west-1"
    encrypt        = true
    dynamodb_table = "ctrl-layer-web-portal-terraform-lock"
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