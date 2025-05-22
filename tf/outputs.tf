output "broker_instance_ids" {
  value = aws_autoscaling_group.kafka_asg.instances
}