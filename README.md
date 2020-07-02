# CloudFormation
This repository contains my CloudFormation configs

## network.yaml
It contains network configuration like:
* VPC
* Subnets
* Internet Gateway
* Route tables

## Apply stack to AWS via CLI
```
aws cloudformation create-stack --stack-name network --template-body file://network.yaml
```

For create or update stack in IAM parameter `--capabilities` is mandatory
```
aws cloudformation create-stack --stack-name iamPacker --template-body file://iam_packer.yaml --capabilities CAPABILITY_NAMED_IAM
```

## Follow stack events
```
aws cloudformation describe-stack-events --stack-name <stack_name>
```


## Destroy stack
```
aws cloudformation delete-stack --stack-name <arn_name>
```

