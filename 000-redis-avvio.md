Redis: Avvio
============

Con rete dedicata
-----------------

Avvio e stop Redis con Docker.

1) Creare una rete dedicata al container Redis


	docker network create redisnet
	
2) Avviare un container collegato alla rete appena creata (--network) con un nome definitio (in questo caso 'redissrv') basato sull'immagine 'redis'.	
Spiegazione:
* `docker`: lancia docker
* `run`: argomento docker per l'avvio di un nuovo container
* `--network <nome-della-network>`: fa si che Docker avvii il container "connettendolo" alla rete il cui nome è specificato. Altri container sulla stessa rete potranno quindi contattarlo.
* `--rm`: fa si che Docker rimuova il container quando questo termina. Va bene per i primi esempi ma è da omettere nel caso si desidera che i dati su Redis sopravvivano al riavvio del container.
* `--name <nome>`: fa si che Docker assegni un nome al container, e che gli altri container collegati alla stessa rete possano usare questo nome per connettercisi. 
* `-d`: parametro opzionale, fa si che Docker lanci il container in background.
* `redis`: nome dell'immagine su cui basare il container da lanciare. In questo caso "redis".

	
	docker run --network redisnet --rm --name redissrv -d redis
	
3) Avviare il client testuale 'redis-cli' anch'esso presente nell'immagine Docker di Redis.
Spiegazione:
* `-it`: argomenti tecnici docker che permettono di inviare i dati da tastiera allo standard in del processo. Permette, in ultima analisi, di interagire via tastiera con il software dockerizzato.
* `redis redis-cli`: come nel caso precedente `redis` è il nome dell'immagine, `redis-cli` è il nome del programma client di redis, anch'esso contenuto nell'immagine Docker `redis`.
* `-h <server redis>`: questo è un parametro di `redis-cli`! Non di Docker!. Fornisce a `redis-cli` il nome dell'host Redis al quale connettersi. E proprio per questo deve essere valorizzato con il valore di `--name` utilizzato per il server.

```shell
	$ docker run -it --network redisnet --rm redis redis-cli -h redissrv
    	redissrv:6379>
```

	
Il server risponde?


```
redissrv:6379> ping
PONG
```
	
Stop Redis con Docker:


	docker stop redissrv	
