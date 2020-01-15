
## Simulating a Stream with Driver Data
 
Please use this guide to load the driver data and the Logic App to simulate a stream.


## Using Cloud Shell

The following bach commands will be ran using the [Azure Cloud Shell](https://docs.microsoft.com/en-us/azure/cloud-shell/overview). 

Launch from Azure portal using the Cloud Shell icon

![cloud shell](../../images/portal-launch-icon.png)

Select __Bash__

![cloud shell](../../images/poverview-choices.png)


## Loading Driver Data

### Create a single instalce Azure SQL Database

Run the following Azure CLI using Cloud Shell to quickly create an Azure SQL Server

```

resourceGroupName=
location=SouthCentralUS
adminLogin=
password=
serverName=hackathon-$RANDOM
databaseName=hackathon


# The ip address range that you want to allow to access your DB. 
# Leaving at 0.0.0.0 will prevent outside-of-azure connections to your DB
startip=0.0.0.0
endip=0.0.0.0


# Create a logical server in the resource group
echo "Creating primary logical server..."
az sql server create \
   --name $serverName \
   --resource-group $resourceGroupName \
   --location $location  \
   --admin-user $adminLogin \
   --admin-password $password

# Configure a firewall rule for the server
echo "Configuring firewall..."
az sql server firewall-rule create \
   --resource-group $resourceGroupName \
   --server $serverName \
   -n AllowYourIp \
   --start-ip-address $startip \
   --end-ip-address $endip


```

### Import BACPAC

Once your Azure SQL Server is created you can quickly create a database using the Driver and Event data by importing a BACPAC file.

__Copy BACPAC file__

```
export AZURE_STORAGE_ACCOUNT="<storage account"
export AZURE_STORAGE_KEY="<sas key>"
container=bacpc

az storage container create --name $container

git clone https://github.com/Jscholtes128/Azure-Streaming-Hackathon.git


az storage blob upload \
    --container-name $container \
    --name TransportEvents-Hack_1_14.bacpac\
    --file 'Azure-Streaming-Hackathon/Steps/01-DataLoad/dependencies/TransportEvents-Hack_1_14.bacpac'
```

__Import BACPAC__

1. To import from a BACPAC file into a new single database using the Azure portal, open the appropriate database server page and then, on the toolbar, select Import database.

![BACPAC](../../images/bacpac1.png)

2. Select the storage account and the container for the BACPAC file and then select the BACPAC file from which to import.

3. Specify the new database size (usually the same as origin) and provide the destination SQL Server credentials. For a list of possible values for a new Azure SQL database, see Create Database.

![BACPAC](../../images/bacpac3.png)

4. Click OK.

5. To monitor an import's progress, open the database's server page, and, under Settings, select Import/Export history. When successful, the import has a Completed status.

![BACPAC](../../images/bacpac4.png)

5. To verify the database is live on the database server, select SQL databases and verify the new database is Online.

_[Import BACPAC](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-import?tabs=azure-powershell) into a Azure SQL Database_


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

