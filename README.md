# Azure Streaming Hackathon

![hackathon design](/images/hackathon.jpg)

Let’s get hands-on with implementing a lambda architecture in Azure using Azure Stream Analytics and Azure Event Hubs. We’ll send-out real-time notification against our real-time stream while preserving all the data for future discovery and analytics.

__Objectives:__

- Implement real-time alerting with Azure Event Hubs, Stream Analytics, Service Bus and Logic Apps.
- Lambda architecture with a 'hot' path for real-time alerting and a 'cold' path for data archiving.
- Use Azure SQL Database to store reference date to include during stream processing.

![hackathon design](/images/hackathon_design.png)

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
