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

Esempio
-------
Estrazione automatizzata lotteria.
Le persone comprano i biglietti della lotteria.
Ogni bilgietto ha un acquirente, un acquirente può comprare più biglietti.
Estrarre 3 biglietti a cui corrispondono 3, 2, 1 premio.
Si deve anche sapere a chi consegnare il premio! perchè è una lotteria autmatizzata.
