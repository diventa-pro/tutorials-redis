#1
contatto:<nome cognome>:telefono => +39121212
contatto:<nome cognome>:email => ddd@ddd.com
contatto:<nome cognome>:creazione => 12345

#2
contatto:<nome cognome>:registro => [ <timestamp chiamata>, <timestamp chiamata> ]

#3
contatto:<nome cognome>:registro => [ registro:1, registro:2 ]

registro:nextid
registro:1:orario =>
registro:1:isincoming => true / false

#3 bis
contatto:<nome cognome>:registro => [ registro:<timestamp>, registro:<timestamp> ]

registro:<timestamp>:orario =>
registro:<timestamp>:isincoming => true / false

#4
contatto:<nome cognome> => { telefono: email: creazione: }
registro:<timestamp> => { timestamp: isIncoming: isLost: number: isBlocked:}

#5
blocked:incoming:  set{'+390000', '+144'}
blocked:outgoing:  set{''}'

#6
contatto:<nome cognome> => zset numero chiamate
