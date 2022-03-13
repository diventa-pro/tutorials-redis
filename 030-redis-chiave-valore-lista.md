Redis: Chiave-Valore Lista
=============================

	rpush series discovery mandalorian "casa di carta"
	llen serie
	
	> lindex series 0
	"discovery"
	
	lpush series "the expanse"
	> lindex serie 0
	
    # L'ultimo
	lindex series -1

    # Il penultimo
    lindex series -2
	
    # Elementi dal primo indice all'ultimo compresi
	lrange series 0 2
	
    # Aggiunge in testa
    lpush
    # Rimuove dalla testa
	lpop series 
	
    # Aggiunge in code
	rpop serie
    # Rimuove dalla coda 
    lpop series

Esempio
-------
Centralino VoIP. Elenco degli orari delle chiamate da un numero.

    rpush inbound:+393401111111 "2021-02-12 23:44:11" "2021-02-13 12:00:00"  

Esercizio 
---------
Pensare a come usare Redis per supportare un sistema di gestione prezzi supermercato.

Scrivere esempi che associano al numero seriale di un dispositivo
di lettura codici prodotto (tecnicamente chiamato dispositivo di self check-out) 
la lista dei numeri seriali dei prodotti in fase di acquisto.

