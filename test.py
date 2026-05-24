import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("PlusTourSparkTest")
    .master("local[*]")
    .getOrCreate()
)

data = [
    (1, "Athens"),
    (2, "Melbourne"),
    (3, "London"),
]

df = spark.createDataFrame(data, ["id", "city"])

print("Spark is running successfully.")
df.show()

spark.stop()