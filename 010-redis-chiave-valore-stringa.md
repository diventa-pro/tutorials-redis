Redis: Chiave-Valore Stringa 
=============================

Impostare e recuperare chiavi stringa.
Lo schema è:

    set <chiave> <valore>

Esempio, numero camera d'albergo, nominativo ospite.
	
    # imposta chiave / valore
    > set suite Presidente
    # Se il valore contiene degli spazi è necessario marcare l'inizio e la fine.
    > set camera10 "Gianni Gialli"
	> set camera11 "Rosa Rossi"
    > set camera21 "Vittorio Verdi" 

	# recupera valore
	> get suite
    > get camera11
    
Se la chiave non esiste.

    > get nonesiste
    (nil)

Cosa accede se si imposta una stessa 
chiave una seconda volta con un valore diverso?
Redis cancella la chiave e il corrispondente valore.

	# cancella
    > del suite
	> del nonesiste

	# multiset
	> mset 003 Rocco 
	> mset 004 Melissa
	
	# multiget
	> MGET 001 002 003 004 005

Esercizio
---------
Usare redis per memorizzare contatti telefonici.

    set "cotatto:bruno bianchi" +393330011122
    set "cotatto:viola verdi" +393332233344
    set "cotatto:roberta rossi" +393338877766