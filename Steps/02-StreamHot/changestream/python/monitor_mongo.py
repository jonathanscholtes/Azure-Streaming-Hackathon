from pymongo import MongoClient
from azure.eventhub import EventHubProducerClient, EventData
import json
import os


connection_str = os.environ['EVENT_HUB_CONNECTION_STR']
eventhub_name = os.environ['EVENT_HUB_NAME']
cosmos_account = os.environ['COSMOS_ACCOUNT_NAME']
cosmos_pass = os.environ['COSMOS_PASSWORD']
database= os.environ['COSMOS_DATABASE']
collection= os.environ['COSMOS_COLLECTION']

producer_client = EventHubProducerClient.from_connection_string(connection_str, eventhub_name=eventhub_name)

client = MongoClient('mongodb://{}.mongo.cosmos.azure.com:10255/?ssl=true'.format(cosmos_account))
        
db = client[database]
    
db.authenticate(name=cosmos_account,password=cosmos_pass)

pipeline = [{ '$match': { 'operationType': { '$in': ['insert', 'update', 'replace'] } } },
        { '$project': { '_id': 1, 'fullDocument': 1, 'ns': 1, 'documentKey': 1 } }]

#option = {'fullDocument':'updateLookup'}

change_stream = db[collection].watch(pipeline,'updateLookup')

for change in change_stream:
    jsn = str(change)
    print(jsn)
    event_data_batch = producer_client.create_batch()
    event_data_batch.add(EventData(jsn))
    producer_client.send_batch(event_data_batch)



