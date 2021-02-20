Sorted Set
===
Un Sorted Set in Redis è un'insieme di stringhe ordinate in base ad uno score e lessicograficamente.

	> zadd leaders 100 "alice"
	(integer) 1

	> zadd leaders 100 "zed"
	(integer) 1

	> zadd leaders 102 "hugo"
	(integer) 1

	> zadd leaders 101 "max"
	(integer) 1

    > zscore
    > zrank
    > zrevrank

    > zrangebylex
    > zrangebyscore
    > zrevrangebylex
    > zrevrangebyscore
    > zrange 
    > zrevrange
