# Setting up production

We use Docker to deploy the application into production, and the manifest is in docker/Dockerfile.convox

To simplify the management of the Docker containers, we're using a managed docker service, [Convox](https://convox.com/) which 
sets up a secure environment and provides a Heroku like CLI to deploy/manage apps. 

BAcking services such as a database or Redis need to be provisioned separately, and we're using AWS for these.

Deployments are triggered via Github actions.
