Che cos'è Redis?
- un'applicazione che gestische chiavi e valori con un container Docker.
- un'applicazione utente che permette di associare chiavi e corrispondenti valori attraverso la linea di comando.
- un'applicazione server che permette di associare chiavi e corrispondenti valori.

Docker permette di...
Eseguire un processo in isolamento definendone l'ambiente di esecuzione.
Installare ed eseguire lo stesso binario su computer con diverse architetture e sistemi operativi.
Condividere i risultati di un'esecuzione tra diverse macchine virtuali.

Redis è un esempio di:
- key-value store
- document based DB
- graph database
- SQL database

In un'istanza Redis in cui non sia presente alcuna chiave,
qual'è il risultato dell'esecuzione di questi comandi?

    set 12 14
    incr 12

- 15
- 13
- (nil)
- un errore

In un'istanza Redis in cui non sia presente alcuna chiave,
qual'è il risultato dell'esecuzione di questi comandi?

    get 66

- (nil)
- 66
- un errore

In un'istanza Redis in cui non sia presente alcuna chiave,
qual'è il risultato dell'esecuzione di questi comandi?

    set proprietario gianni
    set gianni micra
    get (get proprietario)

- un errore
- micra
- get gianni
- gianni

In un'istanza Redis in cui non sia presente alcuna chiave,
qual'è il risultato dell'esecuzione di questi comandi?

    set proprietario gianni
    set lombardia milano
    set piemonte torino
    set veneto venezia
    get venezia

- (nil)
- venezia
- veneto
- 3

In un'istanza Redis in cui non sia presente alcuna chiave,
qual'è il risultato dell'esecuzione di questi comandi?

    set lombardia milano
    set piemonte torino
    flushall
    set veneto venezia
    get veneto

- (nil)
- venezia
- veneto
- 3

In un'istanza Redis in cui non sia presente alcuna chiave,
qual'è il risultato dell'esecuzione di questi comandi?

    set lombardia milano
    set piemonte torino
    set veneto venezia
    mget piemonte veneto toscana

    1) "torino"
    2) "venezia"
    3) (nil)

    1) "torino"
    2) "venezia"

    1) "torino"
    2) "venezia"
    3) (error)

    1) "torino"
    2) "venezia"
    3) "firenze"

In un'istanza Redis in cui non sia presente alcuna chiave,
qual'è il risultato dell'esecuzione di questi comandi?

    lpush lista promessi "sposi il" ritratto di Dorian Gray "l'amico" ritrovato
    lindex lista 1

- "l'amico"
- "il ritratto di Dorian Gray"
- "sposi"
- "sposi il"
- "promessi"
- "promessi sposi"

In quale di questi contesti è giustificato l'utilizzo di Redis?

- Come cache di altri data storage per velocizzare l'accesso ai dati più spesso utilizzati.
- Come ulteriore livello di sicurezza per rendere più difficoltoso l'accesso non autorizzato a sistemi informatici.
- Come strumento per l'esecuzione di processi in ambienti isolati.
- Come linguaggio di programmazione che permette l'utilizzo di costrutti quali liste e hash.