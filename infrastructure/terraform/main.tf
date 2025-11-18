terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.region
}

# VPC
module "vpc" {
  source = "terraform-aws-modules/vpc/aws"
  cidr   = "10.0.0.0/16"
  azs    = ["${var.region}a", "${var.region}b"]
  public_subnets  = ["10.0.1.0/24"]
  private_subnets = ["10.0.2.0/24"]
}

# ECS Cluster
resource "aws_ecs_cluster" "ltd_cluster" {
  name = "ltd-cluster"
}

# ECR for agents
resource "aws_ecr_repository" "ltd_backend" {
  name = "ltd-backend"
}

# Outputs
output "cluster_name" {
  value = aws_ecs_cluster.ltd_cluster.name
}
