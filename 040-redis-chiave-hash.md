Redis: Chiave-Hash
=============================

	hset movie "title" "the godfather"
	hmset movie "year" 1972 "rating" 9.2 "watchers" 10000000
	hincrby movie "watchers" 3
	hget movie "title"
	hmget movie "title" "watchers"
	hgetall movie
	hdel movie "watchers"
	hgetall movie

Esempio
-------
Centralino VoIP. Registrazione di tutte le interazioni con 
vari numeri, sia inbound che outbound.

Chiamata inbound, si registra la chiamata 
e la si elenca come interazione con un particolare numero.

Telefonata inbound da +393401111111 risposta 

    incr nextId

    hmset call:<x> type inbound lost false timestamp "2021-01-31 14:22:00"
    
    rpush interactions:<+393401111111> call:<x> 

Telefonata outbound a +393401111111 senza risposta

    incr nextId

    hmset call:<x> type outbound lost true timestamp "2021-01-31 16:22:00"

    rpush interactions:<+393401111111> call:<x>
