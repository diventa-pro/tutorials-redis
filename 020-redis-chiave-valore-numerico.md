Redis: Chiave-Valore Numerico
=============================

Impostare e recuperare chiavi stringa.
Lo schema è:

    set <chiave> <valore-numerico>

Valore intero

	> set counter 100
    > get counter
	> incr counter
	> decr counter	

Esempio, aziende e fatturato.
	
    # imposta chiave / valore
    > set apple 23.4
    > set tesla 21.6
    > get apple
    > get tesla
    > incrbyfloat apple 0.34
    > mget apple tesla 
 
