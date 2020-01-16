from pymongo import MongoClient
from azure.eventhub import EventHubProducerClient, EventData
import json

connection_str = '<connection string>
eventhub_name = '<hub>'
producer_client = EventHubProducerClient.from_connection_string(connection_str, eventhub_name=eventhub_name)


client = MongoClient('mongodb://<Cosmos Account>.mongo.cosmos.azure.com:10255/?ssl=true')
        
db = client['<Database>']
    
db.authenticate(name="<Cosmos Account>",password='<Cosmos Password>')

pipeline = [{ '$match': { 'operationType': { '$in': ['insert', 'update', 'replace'] } } },
        { '$project': { '_id': 1, 'fullDocument': 1, 'ns': 1, 'documentKey': 1 } }]

#option = {'fullDocument':'updateLookup'}

change_stream = db['<collection>'].watch(pipeline,'updateLookup')

for change in change_stream:
    jsn = str(change)
    print(jsn)
    event_data_batch = producer_client.create_batch()
    event_data_batch.add(EventData(jsn))
    producer_client.send_batch(event_data_batch)



