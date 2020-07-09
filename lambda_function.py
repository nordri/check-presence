import json
import redis
import os

def lambda_handler(event, context):

    redis_endpoint = os.environ['REDIS_ENDPOINT']

    # connect to redis
    client = redis.Redis(host=redis_endpoint, port=6379)

    # set a key
    client.set('ready', 'true')

    # set expire time
    client.expire('ready', 300)

    return {
        'statusCode': 200,
        'body': json.dumps('Presence updated!')
    }
