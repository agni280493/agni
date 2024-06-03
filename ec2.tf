terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.52.0"
    }
  }
}

provider "aws" { 
  region = "us-east-2"
}

resource "aws_instance" "name" { 
    ami = "ami-0ca2e925753ca2fb4"
    instance_type = "t2.micro"
}