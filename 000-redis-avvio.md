Redis: Avvio
-------------

Avvio e stop Redis con Docker:

	> docker network create redisnet
	> docker run --network redisnet --rm --name redissrv -d redis
    > docker stop redissrv

Client testuale:

    > docker run --network redisnet --rm --name redissrv -d redis
	> docker run -it --network redisnet --rm redis redis-cli -h redissrv
    redissrv:6379>
	
Il server risponde?

	> ping
	PONG