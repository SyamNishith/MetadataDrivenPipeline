# Databricks notebook source
sales_df = spark.table(
    "azurepractisedatabricks.silver.sales_pipeline"
)

products_df = spark.table(
    "azurepractisedatabricks.silver.products"
)

gold_product = sales_df.join(
    products_df,
    sales_df.product == products_df.product,
    "left"
)

# COMMAND ----------

gold_product = gold_product.filter(
    gold_product.deal_stage == "Won"
)

# COMMAND ----------

from pyspark.sql.functions import sum

products_df = products_df.withColumnRenamed(
    "product",
    "product_name"
)

gold_product = sales_df.join(
    products_df,
    sales_df.product == products_df.product_name,
    "left"
)

gold_product_summary = gold_product.groupBy(
    "product_name"
).agg(
    sum("sales_price").alias("total_revenue")
)

display(gold_product_summary)

# COMMAND ----------

gold_product_summary.write \
.format("delta") \
.mode("overwrite") \
.saveAsTable(
    "azurepractisedatabricks.gold.product_revenue"
)

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS azurepractisedatabricks.gold;

# COMMAND ----------

# MAGIC %sql
# MAGIC show tables in azurepractisedatabricks.gold

# COMMAND ----------

accounts_df = spark.table(
    "azurepractisedatabricks.silver.accounts"
)

gold_account = sales_df.join(
    accounts_df,
    "account",
    "left"
)

# COMMAND ----------

gold_account_summary = gold_account.groupBy(
    "sector"
).count()

# COMMAND ----------

gold_account_summary.write \
.format("delta") \
.mode("overwrite") \
.saveAsTable(
    "azurepractisedatabricks.gold.sector_analysis"
)

# COMMAND ----------

gold_agent = sales_df.groupBy(
    "sales_agent",
    "deal_stage"
).count()

# COMMAND ----------

gold_agent.write \
.format("delta") \
.mode("overwrite") \
.saveAsTable(
    "azurepractisedatabricks.gold.sales_agent_performance"
)


# COMMAND ----------

# MAGIC %sql
# MAGIC show tables in azurepractisedatabricks.gold

# COMMAND ----------

# MAGIC %sql
# MAGIC select *
# MAGIC from azurepractisedatabricks.gold.product_revenue

# COMMAND ----------

# MAGIC %sql
# MAGIC select *
# MAGIC from azurepractisedatabricks.gold.sector_analysis

# COMMAND ----------

# MAGIC %sql
# MAGIC select *
# MAGIC from azurepractisedatabricks.gold.sales_agent_performance