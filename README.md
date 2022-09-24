
# Rover_Control

Cette application permet de déplacer un robot via le protocole MQTT

## Pré-Requis ##

En premier aller sur maqiatto.com  et créez vous un compte une fois cela fait
cliquer sur ajouter un topic 

Allez sur http://www.hivemq.com/demos/websocket-client/

Host : maqiatto.com                            
Port : 8883
Username : “Votre_Adresse_Mail” (Mise sur Maqiatto)     
Password : MDP serveur Maqiatto  
Keep Alive : 6000

Ensuite appuyez sur Connect en haut à droite

Dans Subscription :
Entrer “Votre_Adresse_Mail”/”nom_premier_topic”
(Exemple : “blabla@gmail.com/topic”)
et cliquer sur Subscribe

Dans Publish :
Entrer “Votre_Adresse_Mail”/nom_deuxieme_topic” 
(Exemple : “blabla@gmail.com/topic1”)
Ajouter un message par défaut dans la case Message
et cliquer sur Publish


## Etape ##
1) Brancher la carte au PC
2) Ouvrir Thonny Python puis aller dans Outil > Interpréteur > Micro python (générique)
3) Et sélectionner le bon COM 
4) Faite “CTRL C” ou redémarrer la carte plusieurs jusqu'à avoir les chevron >>>
5) Tester le programme
6) Transférer le programme directement dans la carte en cliquant sur les fichiers de la carte et faisant transférer …(a revoir)
7) Placer la carte sur le rover
8) Allez sur Maqiatto.com et HVMQ suivez les instructions
9) Lancer le programme en allant dans les paramètres de la carte exécuter le
10) Lancer l’application et connectez vous au serveur MQTT

Créer avec Python, MIT App Inventor

Copyright © 2022 | Rover Control | Tous Droits Réservés.
