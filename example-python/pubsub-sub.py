import redis

# Si collega ad un Redis e pubblica dei messaggi via pubsub.
# https://redis.readthedocs.io/en/stable/advanced_features.html#publish-subscribe
# Il corrispondente subscriber è in pubsub-sub.py.
# Si possono fare vari esperimenti avviando e stoppando i due programmi.

# Questa funzione sarà usata come "gestore" dei messaggi ricevuti,
# si veda più avanti il metodo subscribe()
def handle_message(message):
    print('Received message: %s' % message['data'])

# Create a redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)
print("connected")

# Create a pubsub instance
pubsub = redis_client.pubsub()
print("pubsub ottenuto")

# Subscribe to a channel
# "**" operator: https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
pubsub.subscribe(**{'my-channel':handle_message})
print("sottoscrizione attiva")

# Listen for incoming messages
for message in pubsub.listen():
    # Messages from subscribed channels are handled by the
    # callback function specified when subscribing
    pass


