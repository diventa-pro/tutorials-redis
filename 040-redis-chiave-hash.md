Redis: Chiave-Hash
=============================

	hset movie "title" "the godfather"
	hmset movie "year" 1972 "rating" 9.2 "watchers" 10000000
	hincrby movie "watchers" 3
	hget movie "title"
	hmget movie "title" "watchers"
	hgetall movie
	hdel movie "watchers"
	hgetall movie
