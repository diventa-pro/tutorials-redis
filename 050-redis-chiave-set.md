Set
===
Un Set in Redis è un'insieme di stringhe senza un ordine prestabilito.

Aggiunge elementi di una lista ad una chiave:

	> sadd gianni:preferiti cotoletta carbonara "risotto alla milanese" "pizza margherita"
	> sadd gianni:preferiti "pizza margherita" polpette	
	
Aggiunge altri elementi ad un'altra chiave chiave:
	
	> sadd anna:preferiti tofu ribollita coratella polpette
	
Restituisce i membri di un insieme:
	
    > smembers anna:preferiti
	
Operazioni su insieme:	
	
    > sinter gianni:preferiti anna:preferiti
    > sdiff gianni:preferiti anna:preferiti
    > sunion gianni:preferiti anna:preferiti
	
Restituisce un membro a caso di un set.	

    > srandmember gianni:preferiti

Constrolla che un membro sia contenuto nel set.

    > sismember gianni:preferiti lasagne

Conta gli elementi in un set

    > scard gianni:preferiti
