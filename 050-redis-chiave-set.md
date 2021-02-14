Set
===
Un Set in Redis è un'insieme di stringhe.

	sadd gianni:preferiti cotoletta carbonara "risotto alla milanese" "pizza margherita"
	sadd gianni:preferiti "pizza margherita" polpette	
	sadd anna:preferiti tofu ribollita coratella polpette
    smembers anna:preferiti
    sinter gianni:preferiti anna:preferiti
    sdiff gianni:preferiti anna:preferiti
    sunion gianni:preferiti anna:preferiti
    srandmember gianni:preferiti
    sismember gianni:preferiti lasagne
    scard gianni:preferiti
