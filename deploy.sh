#!/bin/bash

aws cloudformation package \
    --template-file stack.yaml \
    --s3-bucket $DEPLOY_BUCKET \
    --output-template-file packaged-template.yaml

aws cloudformation deploy \
    --template-file packaged-template.yaml \
    --stack-name christmas-gift-api \
    --capabilities CAPABILITY_IAM
