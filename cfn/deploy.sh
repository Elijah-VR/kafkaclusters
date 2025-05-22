#!/bin/bash
aws cloudformation deploy \
  --template-file template.yaml \
  --stack-name kafka-cfn-stack \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides InstanceType=t3.small