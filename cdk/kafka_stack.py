from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_autoscaling as autoscaling,
)
from constructs import Construct

class KafkaStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        vpc = ec2.Vpc.from_lookup(self, "VPC", vpc_id="vpc-00a22d417f36b6e7e")

        sg = ec2.SecurityGroup(self, "KafkaSG",
            vpc=vpc,
            description="Allow Kafka traffic",
            allow_all_outbound=True,
        )
        sg.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(9092), "Kafka port")

        lt = ec2.CfnLaunchTemplate(self, "KafkaLT",
            launch_template_data=ec2.CfnLaunchTemplate.LaunchTemplateDataProperty(
                image_id="ami-0123456789abcdef0",
                instance_type="t3.small",
                security_group_ids=[sg.security_group_id],
                user_data=cdk.Fn.base64("""
#!/bin/bash
... same init script ...
""")
            )
        )

        autoscaling.CfnAutoScalingGroup(self, "KafkaASG",
            min_size="3",
            max_size="3",
            desired_capacity="3",
            launch_template=autoscaling.CfnAutoScalingGroup.LaunchTemplateProperty(
                launch_template_id=lt.ref,
                version=lt.attr_latest_version_number
            ),
            vpc_zone_identifier=["<subnet-0ffad71c47bf57506>", "<subnet-08453128f96f409c0>", "<subnet-0841fd9b8af9c910e>"]
        )