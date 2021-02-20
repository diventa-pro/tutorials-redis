
	
Chiave valore
-------------


	
Far scadere le chiavi
	
	> expire 001 20
	> ttl 001
	> ttl 001
	> ttl 001
	> mget 001
	1) (nil)
	

	


	


Bitmaps
-------

	> SETBIT visits:2015-01-01 10 1
	(integer) 0
	> SETBIT visits:2015-01-01 15 1
	(integer) 0
	> SETBIT visits:2015-01-02 10 1
	(integer) 0
	> SETBIT visits:2015-01-02 11 1	
	
	> GETBIT visits:2015-01-01 10
	(integer) 1

Conta i bit 1 in una chiave

	> BITOP OR total_users visits:2015-01-01 visits:2015-01-02
	> BITCOUNT total_users
	
	> BITCOUNT visits:2015-01-01
	(integer) 2	
	
HyperLogLogs
------------
A HyperLogLog is not actually a real data type in Redis. 
Conceptually, a HyperLogLog is an algorithm that uses randomization in order to provide a very good approximation of the number of unique elements that exist in a Set. 
It is fascinating because it only runs in O(1), constant time, and uses a very small amount of memory—up to 12 kB of memory per key. 
Although technically a HyperLogLog is not a real data type, we are going to consider it as one because Redis provides specific commands to manipulate Strings in order to calculate the cardinality of a set using the HyperLogLog algorithm.	

Comandi

The prefix PF is in honor of Philippe Flajolet, the author of the algorithm. He passed away in March 2011.

	PFADD, PFCOUNT, and PFMERGE.

	PFADD visits:2015-01-01 "carl" "max" "hugo" "arthur"
	PFADD visits:2015-01-01 "max" "hugo"	
	PFADD visits:2015-01-02 "max" "kc" "hugo" "renata"
	PFCOUNT visits:2015-01-01
	
	# Conta la somma di due hyperlogs
	PFCOUNT visits:2015-01-01 visits:2015-01-02
	
	PFMERGE visits:total visits:2015-01-01 visits:2015-01-02
	
Transazioni
-----------
	
marks the beginning of a transaction	
	
	MULTI , 
	
and the command EXEC marks its end.

	EXEC
	
annulla la transazione, cioè non la esegue! non fa rollback!	
	
	DISCARD	
	
Optimistic Lock sulle chiavi all'interno di una transazione	
	
	WATCH / UNWATCH
	
Publish Subscribe
-----------------
	
Sub / unsub ad un canale particolare
	SUBSCRIBE UNSUBSCRIBE
	
Sub / unsub con pattern	
	
	PSUBSCRIBE PUNSUBSCRIBE
	
The command PUBSUB introspects the state of the Redis Pub/Sub system. 
This command accepts three subcommands: CHANNELS, NUMSUB, and NUMPAT.

	PUBSUB CHANNELS [pattern]
	PUBSUB NUMSUB [channel-1 … channel-N]
	PUBSUB NUMPAT
	
Riferimenti
-----------

### Documentazione
https://redis.io/topics/data-types-intro
https://redislabs.com/redis-best-practices/indexing-patterns/geospatial/
https://redis.io/topics/partitioning
	
### GUI
https://www.npmjs.com/search?q=redis-gui
https://github.com/marians/rebrow
https://github.com/mauersu/redis-admin