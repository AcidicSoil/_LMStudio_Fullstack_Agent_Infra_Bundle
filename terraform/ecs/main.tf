provider "aws" {
  region = "us-east-1"
}

resource "aws_ecs_cluster" "lmstudio" {
  name = "lmstudio-agents-cluster"
}

resource "aws_ecs_task_definition" "agents" {
  family                   = "lmstudio-agents"
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  cpu                      = "1024"
  memory                   = "2048"
  execution_role_arn       = var.execution_role_arn

  container_definitions = jsonencode([
    {
      name      = "lmstudio-agents"
      image     = var.image_url
      essential = true
      portMappings = [
        {
          containerPort = 8501
          protocol      = "tcp"
        }
      ],
      environment = [
        { name = "OPENAI_API_KEY", value = "lm-studio" },
        { name = "OPENAI_API_BASE", value = "http://lmstudio:1234/v1" },
        { name = "OPENAI_MODEL_NAME", value = "mistral" },
        { name = "DATABASE_URL", value = var.database_url },
        { name = "REDIS_URL", value = var.redis_url }
      ]
    }
  ])
}

resource "aws_ecs_service" "agents" {
  name            = "lmstudio-agents-service"
  cluster         = aws_ecs_cluster.lmstudio.id
  task_definition = aws_ecs_task_definition.agents.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets         = var.subnet_ids
    security_groups = var.security_group_ids
    assign_public_ip = true
  }
}