from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
import time
import json

time.sleep(15)
while True:
	consumer = KafkaConsumer('new-listings-topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
	for message in consumer:
		new_listing = json.loads((message.value).decode('utf-8'))
		print(new_listing)
	time.sleep(15)