import json
import tweepy
from datetime import datetime
from pyspark.sql.functions import *
import boto3

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAGCOigEAAAAAh1ZVN8%2FS2PcgHrUpChcjVEPTjdg%3D36JPpn7ZfJXyMUTMIfOVUE7lSwzVamRLg9D0yUTjZYQqVYrIjF"

class GetTweets(tweepy.StreamingClient):
    contador = 0
    listajson = []
    s3 = boto3.resource(
        's3',
        region_name='sa-east-1',
        aws_access_key_id='AKIASOHYEFSMFLOURFXW',
        aws_secret_access_key='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'
    )
    def on_connect(self):
        print("Connected")

    def on_tweet(self, tweet):
        if tweet.text.find('…') == -1:
            self.contador += 1
            tjson = {
                "id":tweet.id,
                "tweet_text":tweet.text,
                "tweet_date":tweet['created_at'].strftime('%Y-%m-%d %H:%M:%S')
            }
            self.listajson.append(tjson)
            if self.contador >=100:
                name = tweet['created_at'].strftime('%Y-%m-%d %H-%M-%S')
                self.s3.Object('raw-layer-bucket-xpto', f'tweeter/sa-east-1/tweeter_eleicoes/2022/{name}.json').put(Body=json.dumps(self.listajson,ensure_ascii=False))
                # with open(f's3://raw-layer-bucket-xpto/tweeter/sa-east-1/tweeter_eleicoes/2022/{name}.json', 'w', encoding='utf-8') as f:
                #     json.dump(self.listajson, f, ensure_ascii=False)
                self.contador = 0
                self.listajson = []
            return True
        
keyword = "Bolsonaro"
printer = GetTweets(bearer_token=BEARER_TOKEN)
printer.add_rules(tweepy.StreamRule(keyword))
printer.filter(tweet_fields=['created_at','text','id'])