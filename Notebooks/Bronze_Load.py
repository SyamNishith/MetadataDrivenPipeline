# Databricks notebook source
df = spark.read \
    .option("header", "true") \
    .csv("/Volumes/azurepractisedatabricks/bronze/raw_files/rawdata/accounts.csv")

display(df)

# COMMAND ----------

print(df.count())

# COMMAND ----------

df.printSchema()

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM azurepractisedatabricks.bronze.accounts;

# COMMAND ----------

display(dbutils.fs.ls("/Volumes/azurepractisedatabricks/bronze/raw_files/rawdata/"))

# COMMAND ----------

accounts_df=spark.read.csv("/Volumes/azurepractisedatabricks/bronze/raw_files/rawdata/accounts.csv",header=True,inferSchema=True)

# COMMAND ----------

accounts_df.show()

# COMMAND ----------

accounts_df.printSchema()

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES IN azurepractisedatabricks.bronze;

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS azurepractisedatabricks.bronze.accounts;

# COMMAND ----------

accounts_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("azurepractisedatabricks.bronze.accounts")

# COMMAND ----------

# MAGIC %sql
# MAGIC show tables in azurepractisedatabricks.bronze;
# MAGIC     
# MAGIC

# COMMAND ----------

products_df=spark.read.csv("/Volumes/azurepractisedatabricks/bronze/raw_files/rawdata/products.csv",header=True,inferSchema=True)

# COMMAND ----------

products_df.write.format("delta").mode("overwrite").saveAsTable("azurepractisedatabricks.bronze.products")

# COMMAND ----------

# MAGIC %sql
# MAGIC show tables

# COMMAND ----------

# MAGIC %sql
# MAGIC show tables in azurepractisedatabricks.bronze;

# COMMAND ----------

sales_pipeline_df=spark.read.csv("/Volumes/azurepractisedatabricks/bronze/raw_files/rawdata/sales_pipeline.csv",header=True,inferSchema=True)

# COMMAND ----------

sales_pipeline_df.write.format("delta").mode("overwrite").saveAsTable("azurepractisedatabricks.bronze.sales_pipeline")

# COMMAND ----------

# MAGIC %sql
# MAGIC  show tables in azurepractisedatabricks.bronze;

# COMMAND ----------

sales_teams_df=spark.read.csv("/Volumes/azurepractisedatabricks/bronze/raw_files/rawdata/sales_teams.csv",header=True,inferSchema=True)
sales_teams_df.write.format("delta").mode("overwrite").saveAsTable("azurepractisedatabricks.bronze.sales_teams")

# COMMAND ----------

# MAGIC %sql
# MAGIC  show tables in azurepractisedatabricks.bronze;