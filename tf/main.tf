provider "aws" {
  region = "<REGION>"
}

resource "aws_security_group" "kafka_sg" {
  name        = "kafka-sg"
  description = "Kafka brokers SG"
  vpc_id      = var.vpc_id

  ingress {
    from_port   = 9092
    to_port     = 9092
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_launch_template" "kafka_lt" {
  name_prefix   = "kafka-lt-"
  image_id      = "ami-0123456789abcdef0"
  instance_type = var.instance_type
  vpc_security_group_ids = [aws_security_group.kafka_sg.id]

  user_data = base64encode(<<EOF
#!/bin/bash
... init script ...
EOF
  )
}

resource "aws_autoscaling_group" "kafka_asg" {
  launch_template {
    id      = aws_launch_template.kafka_lt.id
    version = "$Latest"
  }
  vpc_zone_identifier = var.subnet_ids
  min_size            = 3
  max_size            = 3
  desired_capacity    = 3
}