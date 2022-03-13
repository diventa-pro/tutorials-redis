Redis: Chiave-Valore Stringa 
=============================

Impostare e recuperare chiavi stringa.
Lo schema del comando è:

    set <chiave> <valore>

Esempio, numero camera d'albergo, nominativo ospite.
	
    # imposta chiave / valore
    > set suite Presidente
	
    # Se il valore contiene degli spazi 
	# è necessario marcare l'inizio e la fine.
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
	
Ricercare tra le chiavi esistenti

	> keys <pattern>

Esercizio 
---------
Utilizzare Redis come rubrica delle chiamate in entrata.
Serve associare ad ogni numero in ingresso un nominaitvo e poterlo recuperare.

    set "+393401111111" "Bruno Bianchi"
    set "+393402222222" "Viola Verdi"
    set "+393403333333" "Roberta Rossi"

Arriva una chiamata da +393402222222, qual'è il chiamante?

    get "+393402222222"

Arriva una chiamata da +393405555555, qual'è il chiamante?

    get "+393405555555"

Esercizio 
---------
Redis come db chiave-valore per un sistema di gestione prezzi supermercato.
Scrivere esempi per associare il codice prodotto alla descrizione.
Ad esempio 8076809501231 è il codice prodotto (tecnicamente chiamato SKU) di "MULINO BIANCO CAMILLE GR.304".


