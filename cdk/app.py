#!/usr/bin/env python3
import aws_cdk as cdk
from kafka_stack import KafkaStack

def main():
    app = cdk.App()
    KafkaStack(app, "KafkaCdkStack", env=cdk.Environment(account="<ACCOUNT_ID>", region="<REGION>"))
    app.synth()

if __name__ == "__main__":
    main()