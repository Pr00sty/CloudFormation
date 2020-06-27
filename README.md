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

## Follow stack events
```
aws cloudformation describe-stack-events --stack-name <stack_name>
```


## Destroy stack
```
aws cloudformation delete-stack --stack-name <arn_name>
```

