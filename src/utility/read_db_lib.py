import os
from dotenv import load_dotenv
from src.utility.helpers import read_query

load_dotenv()

# print(creds)
# print(os.getenv("USER_NAME"))
# print(os.getenv("DB_PASSWORD"))
# print(os.getenv("DRIVER_CLASS"))
# print(os.getenv("URL"))

def read_db(spark,config, dir_path):
    if config['transformation'][0].upper() == 'Y' and config['transformation'][1].upper() == 'SQL':
        query = read_query(dir_path)
        df = spark.read.format("jdbc") \
            .option("url", os.getenv("URL")) \
            .option("user", os.getenv("USER_NAME")) \
            .option("password", os.getenv("DB_PASSWORD")) \
            .option("query", query) \
            .option("driver", os.getenv("DRIVER_CLASS")) \
            .load()
        return df
    else:
        df = spark.read.format("jdbc") \
            .option("url", os.getenv("URL")) \
            .option("user", os.getenv("USER_NAME")) \
            .option("password", os.getenv("DB_PASSWORD")) \
            .option("dbtable", config['table']) \
            .option("driver", os.getenv("DRIVER_CLASS")) \
            .load()
        return df

