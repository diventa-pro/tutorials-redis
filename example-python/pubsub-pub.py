import random
import time
import redis

# Si collega ad un Redis e pubblica dei messaggi via pubsub.
# https://redis.readthedocs.io/en/stable/advanced_features.html#publish-subscribe
# Il corrispondente subscriber è in pubsub-sub.py.
# Si possono fare vari esperimenti avviando e stoppando i due programmi.

# Create a redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)
print("connesso")

# Create a pubsub instance
pubsub = redis_client.pubsub()
print("pubsub ottenuto")

for i in range(10):
    randint = random.randint(0, 4)
    time.sleep(randint)
    message = 'Hello, World:' + str(randint)
    redis_client.publish('my-channel', message)
    print("messaggio pubblicato")


