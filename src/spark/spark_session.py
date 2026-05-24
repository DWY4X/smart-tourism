import os
import sys
from pyspark.sql import SparkSession


def create_spark_session(app_name="PlusTourPySpark"):
    """
    Create a local Spark session for Windows + VS Code/Jupyter.
    Forces PySpark workers to use the current Python environment.
    """

    os.environ["PYSPARK_PYTHON"] = sys.executable
    os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

    spark = (
        SparkSession.builder
        .appName(app_name)
        .master("local[*]")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("WARN")

    return spark