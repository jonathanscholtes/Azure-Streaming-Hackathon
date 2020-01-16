# Change streams in Azure Cosmos DB’s API for MongoDB

Change feed support in Azure Cosmos DB’s API for MongoDB is available by using the change streams API.

mongo DB 3.6 is supported, not 3.2.

Change Stream Container code is located in the [python](python/) directory.

Docker Containers have been pushed to [jscholtes/cosmosdb.changestream.python](https://hub.docker.com/repository/docker/jscholtes/cosmosdb.changestream.python/general)

## Create Azure Container Instance using Docker Image

```bash
az container create -g MyResourceGroup --name myapp --image jscholtes/cosmosdb.changestream.python:v1 --cpu 1 --memory 1 --environment-variables EVENT_HUB_CONNECTION_STR='<>' EVENT_HUB_NAME='<>' COSMOS_ACCOUNT_NAME='<>' COSMOS_PASSWORD='<>' COSMOS_DATABASE='<>' COSMOS_COLLECTION='<>'
```
