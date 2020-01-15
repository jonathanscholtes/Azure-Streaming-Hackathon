# Azure-Streaming-Hackathon
Hackathon to develop cold path and hot path Azure architecture

## Hackathon steps

## [Step 1 -Azure Resource Prerequisites](Steps/01-PreReq/) 
Get all resources set-up to begin loading data for the Azure Stream Analytics Lambda Hack

## [Step 2-Streaming Data and Reference Data](Steps/02-DataLoad/)
Simulate a stream of driver event data using Azure SQL DB and and Azure Logic App

## [Step 3-Stream Processing Hot Path](Steps/03-StreamHot)
Utilized Azure Event Hubs for real-time stream ingestions and Azure Stream Analytics to identify messegaes for alerting. Alerts will be sent to Azure Service Bus for an event driven notification workflow.

## [Step 4-Stream Processing Cold Path](Step/04-StreamHot)
Leverage a second Azure Stream Analytic job to copy all real-time streaming messages into storage to faciliate reporting and analytics.

