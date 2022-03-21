# https://redis.io/commands/zincrby
# https://redis.readthedocs.io/en/latest/commands.html#core-commands
import redis

def nuova_proposta(redis, descrizione, proponenti):
	proposta = {}	
	proposta["descrizione"] = descrizione
	proposta["proponenti"] = proponenti
	nextId = redis.incr("nextid")
	idProposta =  f"proposta:{nextId}"
	num = redis.hset(idProposta, mapping=proposta)
	print(f"{num} fields added in hash for {idProposta}")
	redis.zadd("voti", {idProposta: 0})
	print(f"Votes for {idProposta} initialized to 0")
	return idProposta
	
def vota_per(redis, idProposta):
	print(f"Casting vote for {idProposta}")
	r = redis.zincrby("voti", 1, idProposta)
	print(f"Cast vote for {idProposta}: {r}")
	return r
	
def exitpoll(redis):
	return redis.zrange("voti", 0, -1, withscores=True, desc=True)

if __name__ == '__main__':

	print("connecting to redis")
	redis = redis.Redis(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True)
	redis.ping()
	print("connected to redis")
	
	scelta = None
	while(scelta != "q"):
		scelta = input("> ")

		if(scelta == "init"):
			redis.flushall()
			redis.set("nextid", 0)
			
		elif(scelta == "proposta"):
			nuova_proposta( redis, input("descrizione > "), input("proponenti > "))
		elif (scelta == "vota"):
			idPropostaVotata = input("vota per > ")
			vota_per(redis, idPropostaVotata)
		elif (scelta == "exitpoll"):
			redis.zrange("voti", 0, -1, "WITHSCORES")
		elif (scelta == "auto"):
			idProposte = []
			idProposte.append( nuova_proposta(redis, "Caffè gratis", "Gigi, Giorgio") )
			idProposte.append( nuova_proposta(redis, "Pranzi gratis", "Anna, Aurelia") )
			idProposte.append( nuova_proposta(redis, "Campo da calcetto", "Sebastiano") )
			vota_per(redis, idProposte[0])
			vota_per(redis, idProposte[1])
			vota_per(redis, idProposte[1])
			vota_per(redis, idProposte[2])
			vota_per(redis, idProposte[2])
			vota_per(redis, idProposte[2])
			print( f"{exitpoll(redis)}" )
