#!/bin/bash

aws cloudformation package \
    --template-file stack.yaml \
    --s3-bucket $DEPLOY_BUCKET \
    --output-template-file packaged-template.yaml

aws cloudformation deploy \
    --template-file packaged-template.yaml \
    --stack-name $STACK_NAME \
    --capabilities CAPABILITY_IAM

echo "API endpoint: $(aws cloudformation describe-stacks --stack-name $STACK_NAME --query 'Stacks[0].Outputs[?OutputKey==`GiftsEndpoint`].OutputValue' --output text)"
