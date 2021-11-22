import json
from kafka import KafkaProducer
from django.conf import settings


# Messages will be serialized as JSON
def serializer(message):
    return json.dumps(message).encode('utf-8')


# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=settings.KAFKA_SERVER,
    value_serializer=serializer
)


def produce_message(topic, partition):
    producer.send(topic, {
        'user_email': partition['user_email'],
        'subject': partition['subject'],
        'message': partition['message']
    })