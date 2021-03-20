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
 
Esempio
-------
Centralino VoIP. Contare il numero di chiamate da ogni numero.

    set +393403333333 1

Questo non va bene, perchè la chiave entra in conflitto con 
una chiave preesistente dall'esercizio precedente. Quindi useremo
le chiavi 

    caller:+393404444444

per associare il numero al nominativo e

    count:+393404444444

per il numero di chiamate

    set count:+393403333333 1
    incr count:+393403333333 1

quante chiamate abbiamo fatto ad un certo numero?

    get count:+393403333333

Esercizio 
---------
Redis come back-end per un sistema di gestione prezzi supermercato.
Scrivere esempi per associare il codice prodotto al prezzo e alla quantità
disponibile.

![Numero Prodotto - Prezzo](https://lh3.googleusercontent.com/proxy/3BffXrpcvh1LT3wjfzZPR5TasldGt6mTaYIx-i8UkmyXFoJWfq4aH11_mJK9eauob-kPh0JrgUxNBnzDEbUSog)

