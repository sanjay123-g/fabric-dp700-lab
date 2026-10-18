# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "f61acf15-6097-4cef-89b4-3bc94d83df95",
# META       "default_lakehouse_name": "lh_practice",
# META       "default_lakehouse_workspace_id": "7cc23e9b-b268-4eb0-ae9d-c3c7a3e3e84c",
# META       "known_lakehouses": [
# META         {
# META           "id": "f61acf15-6097-4cef-89b4-3bc94d83df95"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
spark.range(1000000).count()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

spark.range(1000).write.mode("overwrite").saveAsTable("diag_test")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************
