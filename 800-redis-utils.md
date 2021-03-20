Redis Comandi di utilità
========================

Cambiare "DB"
-------------

	> select [0-16]

Cancellare le chiavi
--------------------

Cancella tutte le chiavi in tutti i db

	> flushall

Cancella le chiavi nel database corrente

	> flushdb

Chiave valore
-------------
	
Far scadere le chiavi: `expire <chiave> <tempo-in-secondi>`
	
	> expire 001 20
	> ttl 001
	> ttl 001
	> ttl 001
	> mget 001
	1) (nil)
		
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