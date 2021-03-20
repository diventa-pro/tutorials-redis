Redis: Avvio
============

Con rete dedicata
-----------------

Avvio e stop Redis con Docker:

	> docker network create redisnet
	> docker run --network redisnet --rm --name redissrv -d redis

Client testuale:

	> docker run -it --network redisnet --rm redis redis-cli -h redissrv
    redissrv:6379>
	
Il server risponde?

	> ping
	PONG
	
Stop Redis con Docker:

    > docker stop redissrv	