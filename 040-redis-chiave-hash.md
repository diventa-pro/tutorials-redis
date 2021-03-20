Redis: Chiave-Hash
=============================

Associa un valore di tipo hash con una proprietà ad una chiave:

	hset movie "title" "the godfather"

Associa / modifica un valore di tipo hash ad una chiave aggiungendo più proprietà:

	hmset movie "year" 1972 "rating" 9.2 "watchers" 10000000

Incrementa una proprietà di tipo numerico:

	hincrby movie "watchers" 3

Restituisce una proprietà / multiple proprietà di un valore hash:

	hget movie "title"
	hmget movie "title" "watchers"
	hgetall movie
	hgetall movie

Cancella una proprietà hash:

	hdel movie "watchers"

Esercizio
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

Esercizio 
---------
Redis come back-end per un sistema di gestione prezzi supermercato.
Scrivere esempi per associare al numero seriale di una tessera socio / punti
i dati dell'intestatario della tessera.

