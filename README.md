# Gift Idea as a Service (GaaS)

A Serverless Gift Idea Generator using AWS SAM.

As seen on [Gift Idea as a Service: a Serverless approach](https://medium.com/poka-techblog/gift-idea-as-a-service-a-serverless-approach-1a46dca0e2ce)

## Deployment

`DEPLOY_BUCKET={a S3 bucket you own} STACK_NAME={choose a stack name} ./deploy.sh`

e.g.

`DEPLOY_BUCKET=my-personal-deploy-bucket STACK_NAME=christmas-gift-api ./deploy.sh`

# Testing

Once your GaaS is deployed, you can invoke it using the URL provided by the `GiftsEndpoint` output of your CloudFormation Stack. 
