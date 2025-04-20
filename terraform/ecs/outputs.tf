output "ecs_cluster_id" {
  value = aws_ecs_cluster.lmstudio.id
}

output "ecs_service_name" {
  value = aws_ecs_service.agents.name
}

output "task_definition_arn" {
  value = aws_ecs_task_definition.agents.arn
}