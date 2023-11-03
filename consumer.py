# import sys
# sys.path.append(".")

# import os
# import json
from datetime import datetime

from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql import functions as F

# from logger.logger import Logger

KAFKA_ENDPOINT = "kafka:9092"                         #.format(os.getenv("KAFKA_ENDPOINT"), os.getenv("KAFKA_ENDPOINT_PORT"))
KAFKA_TOPIC_ORDERS    = "dbserver1.myCompany.Orders"         #os.getenv("KAFKA_TOPIC_ORDERS")
KAFKA_TOPIC_ORDER_DETAIL    = "dbserver1.myCompany.Order_detail"
KAFKA_TOPIC_INV = "dbserver1.myCompany.Inventory"
KAFKA_TOPIC_PRODUCTS = "dbserver1.myCompany.Products"


# logger = Logger('Kafka-Consumer')

# class Consumer:
#   '''
#     Consume data from Kafka's topic and store into Snowflake 

#     Database: sale_db
#     Schema: sale_lake
#     Table: data_lake
#   '''


spark = SparkSession \
        .builder \
        .master("local[*]") \
        .appName("Consumer") \
        .getOrCreate()

    # self._spark.sparkContext.setLogLevel("ERROR")

def orderDF():
  try:
    df = spark \
          .readStream \
          .format("kafka") \
          .option("kafka.bootstrap.servers", KAFKA_ENDPOINT) \
          .option("subscribe", KAFKA_TOPIC_ORDERS) \
          .option("startingOffsets", "earliest") \
          .option("kafka.group.id", "consumer1") \
          .load()

    df = df.selectExpr("CAST(value AS STRING)")
    # schema = StructType([
    #             StructField("email", StringType(), False),
    #             StructField("firstname", StringType(), False),
    #             StructField("id", IntegerType(), False),
    #             StructField("lastname", StringType(), False),
    #             StructField("username", StringType(), False),
    #     ])
    schema = StructType([
                StructField("created_at", StringType(), False),
                StructField("id", IntegerType(), False),
                StructField("product_id", IntegerType(), False),
                StructField("quantity", IntegerType(), False),
        ])
    
    df = df.select(F.from_json(F.col("value"), schema).alias("data")).select("data.*")
    df = df.withColumnRenamed("id","order_id").withColumn("created_at", lit(datetime.now())).withColumnRenamed("created_at","order_created_at")

    # df.printSchema()

      # logger.info(f"Consume topic: {KAFKA_TOPIC}")
  except Exception as e:
      # logger.error(e)
    print(e)

  return df



def orderDetailDF():
  try:
    df = spark \
          .readStream \
          .format("kafka") \
          .option("kafka.bootstrap.servers", KAFKA_ENDPOINT) \
          .option("subscribe", KAFKA_TOPIC_ORDER_DETAIL) \
          .option("startingOffsets", "earliest") \
          .option("kafka.group.id", "consumer2") \
          .load()
      
    # df.printSchema()  

    df = df.selectExpr("CAST(value AS STRING)")

    schema = StructType([
                StructField("id", IntegerType(), False),
                StructField("order_id", IntegerType(), False),
                StructField("payment", StringType(), False),
                StructField("total", IntegerType(), False),
                StructField("user_id", IntegerType(), False),
        ])
    
    df = df.select(F.from_json(F.col("value"), schema).alias("data")).select("data.*")
    df = df.withColumnRenamed("id","detail_id")

    # df.printSchema()

      # logger.info(f"Consume topic: {KAFKA_TOPIC}")
  except Exception as e:
      # logger.error(e)
    print(e)

  return df



def inventoryDF():
  try:
    df = spark \
          .readStream \
          .format("kafka") \
          .option("kafka.bootstrap.servers", KAFKA_ENDPOINT) \
          .option("subscribe", KAFKA_TOPIC_INV) \
          .option("startingOffsets", "earliest") \
          .option("kafka.group.id", "consumer7") \
          .load()
      

    df = df.selectExpr("CAST(value AS STRING)")

    schema = StructType([
                StructField("id", IntegerType(), False),
                StructField("quantity", IntegerType(), False),
        ])
    
    df = df.select(F.from_json(F.col("value"), schema).alias("data")).select("data.*")
    df = df.withColumnRenamed("quantity","inv_quantity")


      # logger.info(f"Consume topic: {KAFKA_TOPIC}")
  except Exception as e:
      # logger.error(e)
    print(e)

  return df



def productsDF():
  try:
    df = spark \
          .readStream \
          .format("kafka") \
          .option("kafka.bootstrap.servers", KAFKA_ENDPOINT) \
          .option("subscribe", KAFKA_TOPIC_PRODUCTS) \
          .option("startingOffsets", "earliest") \
          .option("kafka.group.id", "consumer8") \
          .load()
      

    df = df.selectExpr("CAST(value AS STRING)")

    schema = StructType([
                StructField("category", StringType(), False),
                StructField("created_at", StringType(), False),
                StructField("id", IntegerType(), False),
                StructField("inventory_id", IntegerType(), False),
                StructField("make", StringType(), False),
                StructField("model", StringType(), False),
                StructField("year", StringType(), False),
        ])
    
    df = df.select(F.from_json(F.col("value"), schema).alias("data")).select("data.*")


      # logger.info(f"Consume topic: {KAFKA_TOPIC}")
  except Exception as e:
      # logger.error(e)
    print(e)

  return df




def save_to_data_lake(batch_df, batch_id):
  batch_df.show(5)
  tableName = "speedView_" + str(datetime.now().day) + "_" + str(datetime.now().month) + "_" + str(datetime.now().year)

  batch_df.write \
          .format("jdbc")\
          .option("driver","com.mysql.cj.jdbc.Driver")\
          .option("url", "jdbc:mysql://mysql_des:3306/myCompany")\
          .option("dbtable", tableName)\
          .option("user", "root")\
          .option("password", "debezium")\
          .mode("append")\
          .save()
      

  

# orders_df = consume_from_kafka()
# order_detail_df = orderDetailDF()
# df = orders_df.join(order_detail_df, orders_df.order_id == order_detail_df.order_id, 'inner').drop(order_detail_df.order_id)
# df.printSchema()
# df = productsDF()
# stream = df \
#             .writeStream \
#             .format("console") \
#             .outputMode("append") \
#             .start()\
#             .awaitTermination()

def run():
      products_df = spark.read.format("jdbc")\
                              .option("driver","com.mysql.cj.jdbc.Driver")\
                              .option("url", "jdbc:mysql://mysql:3306/myCompany")\
                              .option("dbtable", "Products")\
                              .option("user", "root")\
                              .option("password", "debezium")\
                              .load()
      
      inventory_df = spark.read.format("jdbc")\
                              .option("driver","com.mysql.cj.jdbc.Driver")\
                              .option("url", "jdbc:mysql://mysql:3306/myCompany")\
                              .option("dbtable", "Inventory")\
                              .option("user", "root")\
                              .option("password", "debezium")\
                              .load()
      inventory_df = inventory_df.withColumnRenamed("quantity","inv_quantity")
      # .drop(order_detail_df.order_id)


      # products_df = productsDF()
      # inventory_df = inventoryDF()
      orders_df = orderDF()
      order_detail_df = orderDetailDF()
      preDF = orders_df.join(order_detail_df, orders_df.order_id == order_detail_df.order_id, 'inner')\
                    .join(products_df, orders_df.product_id == products_df.id, 'inner')\
                    .join(inventory_df, products_df.inventory_id == inventory_df.id, 'inner')

      df = preDF.select("product_id", "Make", "Model", "Category", "quantity", "total", "inv_quantity", "order_created_at")

      stream = df\
            .writeStream \
            .trigger(processingTime='5 seconds') \
            .foreachBatch(save_to_data_lake) \
            .option('spark.sql.streaming.checkpointLocation', '/tmp/stream/checkpoint')\
            .outputMode("append") \
            .start()

      stream.awaitTermination()

run()



# if __name__ == '__main__':
#   Consumer().run()