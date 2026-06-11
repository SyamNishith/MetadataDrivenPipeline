# End-to-End Azure Data Engineering Project Using Medallion Architecture

## Project Overview

This project demonstrates an end-to-end Azure Data Engineering solution that ingests data from an On-Premises SQL Server, processes it through a Medallion Architecture (Bronze, Silver, Gold) using Azure Databricks and Delta Lake, and delivers business insights through Power BI dashboards.

The entire workflow is orchestrated using Azure Data Factory with a metadata-driven pipeline design.

---

## Architecture

SQL Server (On-Premises)
→ Azure Data Factory
→ Azure Data Lake Storage Gen2 (Raw Zone)
→ Azure Databricks Bronze Layer
→ Azure Databricks Silver Layer
→ Azure Databricks Gold Layer
→ Power BI Dashboards

---

## Technologies Used

* Azure Data Factory (ADF)
* Azure Data Lake Storage Gen2 (ADLS Gen2)
* Azure Databricks
* Delta Lake
* Unity Catalog
* Power BI
* SQL Server
* Python (PySpark)
* GitHub

---

## Project Workflow

### 1. Data Ingestion

Source data is extracted from an On-Premises SQL Server and loaded into ADLS Gen2 using Azure Data Factory.

Tables Ingested:

* Accounts
* Products
* Sales Pipeline
* Sales Teams

### 2. Metadata-Driven Pipeline

A metadata-driven approach was implemented using:

* Lookup Activity
* ForEach Activity
* Dynamic Parameters
* Copy Activity

This allows ingestion of multiple tables without hardcoding.

### 3. Bronze Layer

Raw CSV files are loaded into Delta Tables without significant transformation.

Bronze Tables:

* bronze.accounts
* bronze.products
* bronze.sales_pipeline
* bronze.sales_teams

### 4. Silver Layer

Data cleansing and standardization performed:

* Duplicate removal
* Null value handling
* Data type standardization
* Data quality validation

Silver Tables:

* silver.accounts
* silver.products
* silver.sales_pipeline
* silver.sales_teams

### 5. Gold Layer

Business-ready curated datasets were created through aggregations and joins.

Gold Tables:

* gold.product_revenue
* gold.sector_analysis
* gold.sales_agent_performance

### 6. Reporting Layer

Power BI dashboards were developed using Gold Layer tables to provide business insights.

Reports Included:

* Executive Dashboard
* Product Performance Dashboard
* Sales Team Dashboard

---

## Azure Data Factory Pipeline

Pipeline Components:

* Lookup Control Table
* ForEach Activity
* Copy Activity
* Bronze Notebook Activity
* Silver Notebook Activity
* Gold Notebook Activity

Pipeline Flow:

Lookup
→ ForEach
→ Copy SQL Server Data to ADLS
→ Bronze Notebook
→ Silver Notebook
→ Gold Notebook

---

## Databricks Notebooks

### Bronze_Load

Responsibilities:

* Read raw CSV files
* Create Bronze Delta Tables

### Silver_Load

Responsibilities:

* Clean and validate data
* Create Silver Tables

### Gold_Load

Responsibilities:

* Aggregate business metrics
* Create Gold Tables for reporting

---

## Power BI Dashboards

### Executive Dashboard

KPIs:

* Total Revenue
* Total Products
* Total Customers

### Product Analytics

Visuals:

* Revenue by Product
* Product Performance Analysis

### Sales Performance

Visuals:

* Sales Agent Performance
* Won vs Lost Deals Analysis

---

## Repository Structure

```
Azure-End-to-End-Data-Engineering-Project
│
├── ADF
│   └── MetadataDrivenPipeline.json
│
├── Databricks
│   ├── Bronze_Load.py
│   ├── Silver_Load.py
│   └── Gold_Load.py
│
├── PowerBI
│   └── SalesDashboard.pbix
│
├── Architecture
│   ├── ArchitectureDiagram.png
│   ├── PipelineScreenshot.png
│   └── DashboardScreenshots
│
└── README.md
```

---

## Key Learnings

* Building metadata-driven Azure Data Factory pipelines
* Implementing Medallion Architecture using Delta Lake
* Managing data using Unity Catalog
* Orchestrating Databricks notebooks through ADF
* Creating business-ready datasets for reporting
* Building Power BI dashboards from curated Gold Layer tables

---

## Future Enhancements

* Incremental Data Loading
* Change Data Capture (CDC)
* Azure Key Vault Integration
* CI/CD using Azure DevOps
* Logic Apps Email Notifications
* Data Quality Monitoring Framework

---

## Author

Syam Nisith

Azure Data Engineering Project demonstrating:
ADF | Databricks | Delta Lake | ADLS Gen2 | Power BI | Medallion Architecture
