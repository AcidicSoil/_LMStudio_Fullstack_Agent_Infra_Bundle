variable "execution_role_arn" {
  description = "ECS task execution role ARN"
  type        = string
}

variable "image_url" {
  description = "Docker image URL (e.g. DockerHub)"
  type        = string
}

variable "database_url" {
  description = "PostgreSQL connection URL"
  type        = string
}

variable "redis_url" {
  description = "Redis connection URL"
  type        = string
}

variable "subnet_ids" {
  description = "List of subnet IDs for ECS service"
  type        = list(string)
}

variable "security_group_ids" {
  description = "List of security group IDs for ECS service"
  type        = list(string)
}

variable "db_password" {
  description = "Password for RDS PostgreSQL instance"
  type        = string
  sensitive   = true
}

variable "db_subnet_group_name" {
  description = "Subnet group for RDS"
  type        = string
}

variable "redis_subnet_group_name" {
  description = "Subnet group for ElastiCache Redis"
  type        = string
}