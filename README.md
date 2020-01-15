# Azure Streaming Hackathon
Design a Lambda architecture to capture data for batch processing and take immediate action on a real-time data stream to send alerts.

__Objectives:__
- Develop real-time SMS alerting for speeding drivers with Azure Event Hubs, Stream Analytics, Service Bus and Logic Apps.
- Develop a Lambda solution using Azure Stream Analytics to use a 'hot' path for immediate processing and a 'cold' path for data archiving.
- Use an Azure SQL DB reference dataset during stream processing

![hackathon design](image/hackathon_design.png)

_see_ _[Azure Big Data Lambda Architectures](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/#lambda-architecture)_

_[Azure Stream Analytics Lambda Architecture](https://docs.microsoft.com/en-us/azure/stream-analytics/stream-analytics-solution-patterns#lambda-architectures-or-backfill-process)_

## [Hackathon Prerequisites](Steps/00-PreReq/)
Get all resources set-up to begin loading data for the Azure Stream Analytics Lambda Hack

## Hackathon Steps

## [Step 1-Streaming Data and Reference Data](Steps/01-DataLoad/)
Simulate a stream of driver event data using Azure SQL DB and and Azure Logic App

## [Step 2-Stream Processing Hot Path](Steps/02-StreamHot)
Utilized Azure Event Hubs for real-time stream ingestions and Azure Stream Analytics to identify messegaes for alerting. Alerts will be sent to Azure Service Bus for an event driven notification workflow.

## [Step 3-Stream Processing Cold Path](Step/03-StreamHot)
Leverage a second Azure Stream Analytic job to copy all real-time streaming messages into storage to faciliate reporting and analytics.

