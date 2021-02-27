#1 
chiave -> valore (stringa)
caso d'uso: 
chiamate ingresso, arriva un numero, mostrare il chiamante / numero se sconosciuto
chiamate ingresso, numero di chiamate ricevute
es:
contatto:<tel1> => gianni Rossi
contatto:<tel2> => gianni Rossi
contatto:<tel3> => Maria Verdi
inbound:<tel1>:count => 0
inbound:<tel3>:count => 0


#2
caso d'uso: lista delle chiamate ricevute
es:
inbound:log => [+390123, +3901234]
outbound:log => [+390123, +3901234]
nuova telefonata in arrivo / in uscita

#3
caso d'uso: lista delle chiamate inbound e outbound x numero di telefono

telefono:<tel1> => [chiamata:1, chiamata:3]
telefono:<tel2> => [chiamata:4, chiamata:5]

chiamata:1 => {
    timestamp:
    isIncoming:
    isLost:
    callee:
    caller:
}

chiamata:2 => {
}

#4
caso d'uso chiamate bloccate

inbound:blocker  set{'+390000', '+144'}
outbound:blocked:  set{''}'
chiamata:1 => {
timestamp:
isIncoming:
isLost:
callee:
caller:
blocked:
}

#5
caso d'uso, numeri più comuni

inbound => zset {
    <+39020202> 13
}
