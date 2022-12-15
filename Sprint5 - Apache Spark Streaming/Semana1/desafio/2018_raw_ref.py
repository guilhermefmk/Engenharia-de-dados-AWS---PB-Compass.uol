from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql import functions as F
from pyspark.sql.functions import *
spark = SparkSession.builder.appName("Loads raw to ref").getOrCreate()


def check_first(text):
    pos_emojis = [':D',':)',':]',':}']
    neg_emojis = [':c',':(',':[',':{']
    index_pos = 1000
    index_neg = 1000
    for emoji_pos in pos_emojis:
        temp = text.find(emoji_pos)
        if temp < index_pos and temp != -1:
            index_pos = temp
    for emoji_neg in neg_emojis:
        temp = text.find(emoji_neg)
        if temp < index_neg and temp != -1:
            index_neg = temp
    result = 'positivo' if index_neg > index_pos and index_neg != 1000 else('negativo' if index_neg < index_pos and index_pos != 1000 else 'erro')
    return result


def get_emogi(text):
    emojis = [':D',':)',':]',':}',':c',':(',':[',':{']
    index = 1000
    emoji_r = ''
    for emoji in emojis:
        temp = text.find(emoji)
        if temp < index and temp != -1:
            emoji_r = emoji
            index = temp
    return emoji_r
    
df = spark.read.csv('s3://raw-layer-bucket-xpto/tweeter/sa-east-1/tweeter_eleicoes/2018/04112022.csv', header=True, inferSchema=True, sep="\u0001")

regex_pos = ":\)|:D|:\]|:\}"
regex_neg = ":\[|:c|:\(|:\{"

checar = udf(check_first, StringType())
getter = udf(get_emogi, StringType())

df = df.select('*').withColumn(
    'sentimento', when(
        (col("tweet_text").rlike(regex_pos)) & (col("tweet_text").rlike(regex_neg)), checar('tweet_text')
    ).when(
        (col("tweet_text").rlike(regex_pos)) & ~(col("tweet_text").rlike(regex_neg)), 'positivo'
    ).when(
        ~(col("tweet_text").rlike(regex_pos)) & (col("tweet_text").rlike(regex_neg)), 'negativo'
    ).when(
        ~(col("tweet_text").rlike(regex_pos)) & ~(col("tweet_text").rlike(regex_neg)), 'neutro'
    )
).withColumn('emoji',
    when(
       col('sentimento') == 'neutro', 'n/a' 
    ).otherwise(
        getter('tweet_text')
    )
)

df = df.filter(
    (df['tweet_date'] != '0002-12-31 00:00:00')
)

df_final = df.withColumn("timestamp", to_timestamp(col("tweet_date"), 'yyyyMMddHHmm')) \
           .withColumn("year", date_format(col("timestamp"), "yyyy")) \
           .withColumn("month", date_format(col("timestamp"), "MM")) \
           .withColumn("day", date_format(col("timestamp"), "dd")) \
           .drop("timestamp")


df_final.write.mode("append").partitionBy("year", "month", "day") \
    .parquet('s3://ref-layer-bucket-xpto/tweeter/sa-east-1/tweeter_eleicoes/')