# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS azurepractisedatabricks.silver;

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW SCHEMAS IN azurepractisedatabricks;

# COMMAND ----------

accounts_df = spark.table(
    "azurepractisedatabricks.bronze.accounts"
)

display(accounts_df)

# COMMAND ----------

accounts_clean = accounts_df.dropDuplicates()

accounts_clean = accounts_clean.na.fill({
    "subsidiary_of":"Unknown"
})

# COMMAND ----------

accounts_clean.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable(
        "azurepractisedatabricks.silver.accounts"
    )

# COMMAND ----------

# MAGIC %sql
# MAGIC show tables in azurepractisedatabricks.silver

# COMMAND ----------

products_df=spark.table(
    "azurepractisedatabricks.bronze.products"
)
display(products_df)

# COMMAND ----------

products_df.printSchema()

# COMMAND ----------



# COMMAND ----------

products_df = products_df.dropDuplicates()

# COMMAND ----------

products_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("azurepractisedatabricks.silver.products")

# COMMAND ----------

sales_pipeline_df=spark.table("azurepractisedatabricks.bronze.sales_pipeline")

# COMMAND ----------

sales_pipeline_df.printSchema()

# COMMAND ----------

display(sales_pipeline_df)

# COMMAND ----------

from pyspark.sql.functions import col, when, to_date



# Remove duplicates
sales_pipeline_df =sales_pipeline_df.dropDuplicates()

# Replace null account names
sales_pipeline_df = sales_pipeline_df.na.fill({
    "account": "Unknown"
})

# Convert dates
sales_pipeline_df = sales_pipeline_df.withColumn(
    "engage_date",
    to_date(col("engage_date"))
)

# Handle '-' close dates
sales_pipeline_df = sales_pipeline_df.withColumn(
    "close_date",
    when(col("close_date") == "-", None)
    .otherwise(col("close_date"))
)

sales_pipeline_df = sales_pipeline_df.withColumn(
    "close_date",
    to_date(col("close_date"))
)

display(sales_pipeline_df)

# COMMAND ----------

sales_pipeline_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable(
        "azurepractisedatabricks.silver.sales_pipeline"
    )

# COMMAND ----------

sales_teams_df=spark.table("azurepractisedatabricks.bronze.sales_teams")

# COMMAND ----------

display(sales_teams_df)

# COMMAND ----------

sales_teams_df.write.format("delta").mode("overwrite").saveAsTable("azurepractisedatabricks.silver.sales_teams")

# COMMAND ----------

# MAGIC %sql
# MAGIC show tables in azurepractisedatabricks.silver