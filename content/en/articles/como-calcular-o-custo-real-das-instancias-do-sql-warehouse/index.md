---
title: "How to Calculate the Real Cost of Azure Databricks SQL Warehouse Instances"
slug: "how-to-calculate-real-cost-azure-databricks-sql-warehouse-instances"
date: 2024-06-29T22:21:00Z
summary: "Shall we learn how to calculate the cost of SQL Warehouse instances in Microsoft Azure Databricks the easy way? Then follow along with this article."
tags: ["SQL", "Azure", "Costs", "Databricks"]
series: ["Ahead of the AI"]
linkedin: "https://www.linkedin.com/pulse/como-calcular-o-custo-real-das-inst%C3%A2ncias-do-sql-warehouse-lopes-t84if"
cover:
  image: cover.png
  alt: "How to Calculate the Real Cost of Azure Databricks SQL Warehouse Instances"
  relative: true
---

Shall we learn how to calculate the cost of SQL Warehouse instances in [Microsoft Azure](https://www.linkedin.com/company/microsoft-azure/) [Databricks](https://www.linkedin.com/company/databricks/) the easy way? Then follow along with this article.

SQL Warehouse in [Databricks](https://www.linkedin.com/company/databricks/) is a tool that lets us query and explore data efficiently.

Currently, [Microsoft Azure](https://www.linkedin.com/company/microsoft-azure/) [Databricks](https://www.linkedin.com/company/databricks/) offers three types of SQL Warehouse:

1. **SQL Warehouse Classic**: This type of SQL Warehouse uses our Azure subscription account. It supports Photon, but not Predictive IO or Intelligent Workload Management.
2. **SQL Warehouse Pro**: Like Classic, it uses our Azure subscription account, but it supports both Photon and Predictive IO. However, it does not support Intelligent Workload Management.
3. **SQL Warehouse Serverless**: This type uses the Azure Databricks serverless architecture and supports every Databricks SQL performance feature, including Photon, Predictive IO and Intelligent Workload Management. It runs directly in our Azure Databricks account.

The main difference between SQL Warehouse Classic, Pro and Serverless is where the compute layer lives and which features are supported. While Classic and Pro use our Azure subscription account, Serverless runs in the [Microsoft Azure](https://www.linkedin.com/company/microsoft-azure/) [Databricks](https://www.linkedin.com/company/databricks/) account and supports more features.

### DIY Method

This section is aimed at developers or technical folks who want to understand the logic behind cost analysis and perhaps build their own tools or scripts to calculate the cost of [Microsoft Azure](https://www.linkedin.com/company/microsoft-azure/) [Databricks](https://www.linkedin.com/company/databricks/) SQL Warehouse instances.

### DIY Method: SQL Warehouse Classic

To calculate the cost of a [Microsoft Azure](https://www.linkedin.com/company/microsoft-azure/) [Databricks](https://www.linkedin.com/company/databricks/) SQL Warehouse Classic or Pro, we need to consider the following components:

1. **SQL compute hours**: The time the SQL Warehouse was running.
2. **Databricks Unit (DBU) hours**: Compute units used by the SQL Warehouse, billed per hour.
3. **Storage costs**: Costs associated with data storage, if applicable.
4. **Bandwidth costs**: Costs associated with data transfer, if applicable.

### Getting the list of classic SQL Warehouse instances from the Databricks API

The first step is to retrieve the list of SQL Warehouse instances using the [Microsoft Azure](https://www.linkedin.com/company/microsoft-azure/) [Databricks](https://www.linkedin.com/company/databricks/) API: /api/2.0/sql/warehouses.

After running the API call, we'll get a JSON response with all the [Microsoft Azure](https://www.linkedin.com/company/microsoft-azure/) [Databricks](https://www.linkedin.com/company/databricks/) SQL Warehouses.

Here's an example of the SQL Warehouse Classic JSON:

```
"warehouses":[
{
  "id":"2b1623d985c31e5d",
  "name":"Classic Warehouse",
  "size":"XXSMALL",
  "cluster_size":"2X-Small",
  "min_num_clusters":1,
  "max_num_clusters":1,
  "auto_stop_mins":45,
  "auto_resume":true,
  "creator_name":"julianamarialopes@hotmail.com",
  "creator_id":1036471208901988,
  "tags":{ },
  "spot_instance_policy":"COST_OPTIMIZED",
  "enable_photon":true,
  "channel":{
    "name":"CHANNEL_NAME_CURRENT"
  },
  "enable_serverless_compute":false,
  "warehouse_type":"CLASSIC",
  "num_clusters":0,
  "num_active_sessions":0,
  "state":"STOPPED",
  "jdbc_url":"jdbc:spark://adb-xxxxxxxx.x.azuredatabricks.net:443/default;transportMode=http;ssl=1;AuthMech=3;httpPath=/sql/1.0/warehouses/2b1623d985c31e5d;",
    "odbc_params":{
      "hostname":"adb-xxxxxxxx.x.azuredatabricks.net",
      "path":"/sql/1.0/warehouses/2b1623d985c31e5d",
      "protocol":"https",
      "port":443
    }
   }
  }
]        
```

### Getting the cost of SQL Warehouse Classic resources from the [Microsoft](https://www.linkedin.com/company/microsoft/) API

To calculate SQL Warehouse Classic costs, we need to combine the usage data with the cost information.

We'll use the [Microsoft Generate Cost Details Report API](https://learn.microsoft.com/en-us/rest/api/cost-management/generate-cost-details-report/create-operation?view=rest-cost-management-2023-11-01&tabs=HTTP) to get all the data from the [Microsoft Azure](https://www.linkedin.com/company/microsoft-azure/) subscription where our [Microsoft Azure](https://www.linkedin.com/company/microsoft-azure/) [Databricks](https://www.linkedin.com/company/databricks/) clusters are running.

Here are some important notes when using this API:

1. **Filtering the data**: We must filter the Databricks-related data and remove any data related to other services or data with no associated cost.
2. **Subscription type**: We need to adjust the results based on the Azure subscription type (pay-as-you-go or enterprise), since the data format may differ.
3. **Data limits**: The API lets you extract data for a period of at most one month and no older than 13 months.

When extracting data from the [Microsoft Azure](https://www.linkedin.com/company/azurecommunity/) API, we select the following columns from the report:

- **SqlEndpointId**: The SQL Warehouse instance ID.
- **ProductName**: Description of the Azure resource consumed.
- **MeterName**: Label identifying the type of service or resource being billed.
- **CostInBillingCurrency**: Cost of the Azure resource consumed.

We'll get data similar to this (formatted for easy reading):

![](img-01.png)

In **SQL Warehouse Classic** instances, **the Product** equals **Azure Databricks - Premium - SQL Analytics** and the **MeterName** equals **Premium SQL Analytics DBU.**

Next, we add up all the records to calculate the final cost of the SQL Warehouse instance.

### DIY Method - SQL Warehouse Pro

To calculate the cost of a [Microsoft Azure](https://www.linkedin.com/company/microsoft-azure/) [Databricks](https://www.linkedin.com/company/databricks/) **SQL Warehouse Pro**, we need to take the following components into account:

1. **SQL compute hours:** the time during which the SQL Warehouse was running.
2. **Databricks Unit (DBU) hours:** the compute units used by the SQL Warehouse, which are billed per hour.
3. **Storage Costs:** Costs associated with data storage, if applicable.
4. **Bandwidth costs:** Costs associated with bandwidth transfer, if applicable.

After running the API call, we'll get a JSON response with all the [Microsoft Azure](https://www.linkedin.com/company/microsoft-azure/) [Databricks](https://www.linkedin.com/company/databricks/) SQL Warehouses.

This is the **SQL Warehouse Pro** JSON:

```
"warehouses":[
{
  "id":"aedd502a567f273a",
  "name":"Starter Warehouse",
  "size":"XXSMALL",
  "cluster_size":"2X-Small",
  "min_num_clusters":1,
  "max_num_clusters":1,
  "auto_stop_mins":10,
  "auto_resume":true,
  "creator_name":"julianamarialopes@hotmail.com",
  "creator_id":1036471128901988,
  "tags":{ },
  "spot_instance_policy":"COST_OPTIMIZED",
  "enable_photon":true,
  "channel":{ },
  "enable_serverless_compute":false,
  "warehouse_type":"PRO",
  "num_clusters":0,
  "num_active_sessions":0,
  "state":"STOPPED",
  "jdbc_url":"jdbc:spark://adb-xxxxxxxx.x.azuredatabricks.net:443/default;transportMode=http;ssl=1;AuthMech=3;httpPath=/sql/1.0/warehouses/aedd502a567f273a;",
    "odbc_params":{
      "hostname":"adb-xxxxxxxx.x.azuredatabricks.net",
      "path":"/sql/1.0/warehouses/aedd502a567f273a",
      "protocol":"https",
      "port":443
    }
   }
  }
]        
```

Very similar to the previous example.

## Getting the cost of SQL Warehouse PRO resources from the Microsoft API

To calculate SQL Warehouse Pro costs, we need to combine the retrieved usage data with the cost information to calculate the total cost.

We'll use the [**Microsoft Generate Cost Details Report API**](https://learn.microsoft.com/en-us/rest/api/cost-management/generate-cost-details-report/create-operation?view=rest-cost-management-2023-11-01&tabs=HTTP) to get all the data from the Azure subscription where our Databricks clusters are running.

Important notes when using the API:

- When we get the cost details data from a [Microsoft Azure](https://www.linkedin.com/company/microsoft-azure/) subscription, we must filter the Databricks-related data and remove any data related to other services and data with no associated cost.
- We need to adjust the results based on the [Microsoft Azure](https://www.linkedin.com/company/microsoft-azure/) **subscription** type **(pay-as-you-go or enterprise)** because the output is different.
- The API only allows data to be extracted for **one month or less** and **no older than 13 months**.

When extracting the data from the Microsoft API, we'll need to select the following columns from the report:

- **SqlEndpointId:** the SQL Warehouse instance ID
- **ProductName:** the description of the Azure resource consumed
- **MeterName:** the label identifying the type of service or resource being billed
- **CostInBillingCurrency:** the cost of the Azure resource consumed
- **BillingCurrency:** the billing currency code (USD, EUR, etc.)

## 1.2.3. Calculating the cost of SQL Warehouse PRO instances

After retrieving the data from [Microsoft Azure](https://www.linkedin.com/company/microsoft-azure/) [Databricks](https://www.linkedin.com/company/databricks/) and from the [Microsoft Azure](https://www.linkedin.com/company/microsoft-azure/) APIs, the final step is to filter the Azure cost data by SQL endpoint ID and match it to the SQL endpoint ID from the [Microsoft Azure](https://www.linkedin.com/company/microsoft-azure/) [Databricks](https://www.linkedin.com/company/databricks/) API.

In **SQL Warehouse Pro** instances, **the Product** equals **Azure Databricks Regional - Premium - SQL Compute Pro** and the **MeterName** equals **Premium SQL Compute Pro DBU.**

Next, we add up all the records to calculate the final cost of the SQL Warehouse instance.

## 1.3. DIY Method: SQL Warehouse Serverless

**[Microsoft Azure](https://www.linkedin.com/company/microsoft-azure/) [Databricks](https://www.linkedin.com/company/databricks/) SQL Warehouse serverless instances** run inside our [Microsoft Azure](https://www.linkedin.com/company/microsoft-azure/) [Databricks](https://www.linkedin.com/company/databricks/) account, so we're billed only in Databricks Unit (DBU) hours.

After running the API call, we'll get a JSON with all the [Microsoft Azure](https://www.linkedin.com/company/microsoft-azure/) [Databricks](https://www.linkedin.com/company/databricks/) SQL Warehouses.

This is the **SQL Warehouse Serverless** JSON:

```
"warehouses":[
{
  "id":"e5e7201bde7c3a43",
  "name":"Serveless Warehouse",
  "size":"XXSMALL",
  "cluster_size":"2X-Small",
  "min_num_clusters":1,
  "max_num_clusters":1,
  "auto_stop_mins":10,
  "auto_resume":true,
  "creator_name":"julianamarialopes@hotmail.com",
  "creator_id":1036471128901988,
  "tags":{ },
  "spot_instance_policy":"COST_OPTIMIZED",
  "enable_photon":true,
  "enable_serverless_compute":true,
  "warehouse_type":"PRO",
  "num_clusters":0,
  "num_active_sessions":0,
  "state":"STOPPED",
  "jdbc_url":"jdbc:spark://adb-xxxxxxxx.x.azuredatabricks.net:443/default;transportMode=http;ssl=1;AuthMech=3;httpPath=/sql/1.0/warehouses/e5e7201bde7c3a43;",
    "odbc_params":{
      "hostname":"adb-xxxxxxxx.x.azuredatabricks.net",
      "path":"/sql/1.0/warehouses/e5e7201bde7c3a43",
      "protocol":"https",
      "port":443
    }
   }
  }
]        
```

## 1.3.2. Getting the cost of SQL Warehouse serverless resources from the Microsoft API

We need to combine the retrieved usage data with the cost information to calculate SQL Warehouse Serverless costs.

We'll use the [**Microsoft Generate Cost Details Report API**](https://learn.microsoft.com/en-us/rest/api/cost-management/generate-cost-details-report/create-operation?view=rest-cost-management-2023-11-01&tabs=HTTP) to get all the data from the Azure subscription where our [Microsoft Azure](https://www.linkedin.com/company/microsoft-azure/) [Databricks](https://www.linkedin.com/company/databricks/) clusters are running.

Important notes when using the API:

- When we get the cost details data from a [Microsoft Azure](https://www.linkedin.com/company/microsoft-azure/) subscription, we must filter the data related to [Microsoft Azure](https://www.linkedin.com/company/microsoft-azure/) [Databricks](https://www.linkedin.com/company/databricks/) and remove any data related to other services and data with no associated cost.
- We need to adjust the results based on the [Microsoft Azure](https://www.linkedin.com/company/microsoft-azure/) **subscription** type **(pay-as-you-go or enterprise)** because the output is different.
- The API only allows data to be extracted for **one month or less** and **no older than 13 months**.

When extracting the data from the [Microsoft](https://www.linkedin.com/company/microsoft/) API, we'll need to select the following columns from the report:

- **SqlEndpointId:** the SQL Warehouse instance ID
- **ProductName:** the description of the Azure resource consumed
- **MeterName:** the label identifying the type of service or resource being billed
- **CostInBillingCurrency:** the cost of the Azure resource consumed
- **BillingCurrency:** the billing currency code (USD, EUR, etc.)

## 1.3.3. Calculating the cost of SQL Warehouse serverless instances

After retrieving the data from [Microsoft Azure](https://www.linkedin.com/company/microsoft-azure/?trk=article-ssr-frontend-pulse_little-text-block) [Databricks](https://www.linkedin.com/company/databricks/?trk=article-ssr-frontend-pulse_little-text-block) and from the
[Microsoft Azure](https://www.linkedin.com/showcase/microsoft-azure/?trk=article-ssr-frontend-pulse_little-mention)
APIs, the final step is to filter the cost data by SQL endpoint ID and match it to the SQL endpoint ID from the [Microsoft Azure](https://www.linkedin.com/company/microsoft-azure/?trk=article-ssr-frontend-pulse_little-text-block) [Databricks](https://www.linkedin.com/company/databricks/?trk=article-ssr-frontend-pulse_little-text-block) API.

In **SQL Warehouse Serverless** instances, **the Product** equals **Azure Databricks Regional - Premium - Serverless SQL** and the **MeterName** equals **Premium Serverless SQL DBU.**

Next, we add up all the records to calculate the final cost of the SQL Warehouse instance.

And that's it, folks. If you enjoyed this article, please show your support 👏. Thanks for reading!
