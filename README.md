# tutorials-redis
Diventa.pro tutorial about Redis

To launch the example...

Launch a redis container

	docker run --network redisnet --name redis --rm -d -p 6379:6379 redis
	docker run -ti --network redisnet redis redis-cli -h redis
	
Set-up the Python env and launch it

	# se virtualenv presente
    virtualenv venv
	
	# se virtualenv non presente
	python -m virtualenv venv
	
	# in MS-DOS
    venv\Scripts\activate.bat
	
    pip install -r requirements.txt
    python main.py