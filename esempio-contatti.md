#1 
chiave -> valore (stringa)
caso d'uso: arriva un numero, mostrare il chiamante / numero se sconosciuto
es:
telefono:<tel1> => gianni Rossi
telefono:<tel2> => gianni Rossi
telefono:<tel3> => Maria Verdi


#2
caso d'uso: lista delle chiamate ricevute
es:
chiamate => [+390123, +3901234]
nuova telefonata in arrivo / in uscita

#3
caso d'uso: lista delle chiamate incoming outgoing x numero di telefono

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

blocked:incoming:  set{'+390000', '+144'}
blocked:outgoing:  set{''}'
chiamata:1 => {
timestamp:
isIncoming:
isLost:
callee:
caller:
blocked:
}

