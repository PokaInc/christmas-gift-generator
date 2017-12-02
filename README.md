# Gift Idea as a Service (GaaS)

A Serverless Gift Idea Generator using AWS SAM.

## Deployment

`DEPLOY_BUCKET={a S3 bucket you own} STACK_NAME={choose a stack name} ./deploy.sh`

e.g.

`DEPLOY_BUCKET=my-personal-deploy-bucket STACK_NAME=christmas-gift-api ./deploy.sh`

# Testing

Once your GaaS is deployed, you can invoke it using the URL provided by the `GiftsEndpoint` output of your CloudFormation Stack. 
