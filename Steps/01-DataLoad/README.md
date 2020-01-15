
## Creating a stream with driver data
 
Please use this guide to load the driver and driver event data for the Azure Streaming Hackathon.


## Loading the driver data

The following bach commands will be ran using the [Azure Cloud Shell](https://docs.microsoft.com/en-us/azure/cloud-shell/overview). 

Launch from Azure portal using the Cloud Shell icon
!(cloud shell)[../../images/portal-launch-icon.png]

## Create a Single Instance Azure SQL Database

- Create a single instance Azure SQL Database, [follow steps here](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-single-database-get-started?tabs=azure-portal).

Load [dependencies/Events.csv](dependencies/) into an Azure Storage Blob, then [Import BACPAC](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-import?tabs=azure-powershell) into a Azure SQL Database 


### Create Messages with Azure Logic Apps

We will use the Cloud Shell to quickly create an Azure Logic App to send our Event Hub Messages.

- Open the cloud shell to Bash.
- Import [dependencies/parameters.json](dependencies/)
- Modify the resource group in the shell script below, then run in the Cloud Shell.

```
resourceGroupName=''
name='EventCreateLogicApp'
templatefile='template.json'


az group deployment create \
  --name $name\
  --resource-group $resourceGroupName \
  --template-file $templatefile 
```

Once the Azure Logic App is created we will need to manually resolve the missing SQL and Event Hub connections.

