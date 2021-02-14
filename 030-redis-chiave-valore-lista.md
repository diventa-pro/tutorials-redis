Redis: Chiave-Valore Lista
=============================

	rpush series htgawm mandalorian "american gods"
	llen serie
	
	> lindex series 0
	"htgawm"
	
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