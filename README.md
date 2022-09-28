![Logo](https://cdn.discordapp.com/attachments/971852061044006922/1023237417471324180/unknown.png)

# Rover_Control

Cette application permet de déplacer un robot via le protocole MQTT

## Pré-Requis ##

En premier aller sur https://www.maqiatto.com/ et créez vous un compte une fois cela fait
cliquer sur ajouter un topic 

![App Screenshot](https://cdn.discordapp.com/attachments/1003942960284573746/1023328771262124072/topic.png)

Allez sur http://www.hivemq.com/demos/websocket-client/

![App Screenshot](https://cdn.discordapp.com/attachments/1003942960284573746/1023328770884653066/HiveMQ.png)

Host : maqiatto.com                            
Port : 8883
Username : “Votre_Adresse_Mail” (Mise sur Maqiatto)     
Password : MDP serveur Maqiatto  
Keep Alive : 6000

Ensuite appuyez sur Connect en haut à droite

![App Screenshot](https://cdn.discordapp.com/attachments/1003942960284573746/1023328771656392834/Connect.png)


Dans Subscription :
Entrer “Votre_Adresse_Mail”/”nom_premier_topic”

![App Screenshot](https://cdn.discordapp.com/attachments/1003942960284573746/1023328770154823762/Subscribe.png)

(Exemple : “blabla@gmail.com/topic”)
et cliquer sur Subscribe


Dans Publish :
Entrer “Votre_Adresse_Mail”/nom_deuxieme_topic” 

(Exemple : “blabla@gmail.com/topic1”)
Ajouter un message par défaut dans la case Message
et cliquer sur Publish
![App Screenshot](https://cdn.discordapp.com/attachments/1003942960284573746/1023328770528125058/Publsih.png)

## Branchement / Configuration  ##
1) Brancher la carte au PC sur un port USB
2) Ouvrir Thonny Python puis aller dans Outil > Interpréteur > Micro python (générique), et sélectionner le bon COM dans Port


![App Screenshot](https://cdn.discordapp.com/attachments/1003942960284573746/1023330656584998982/AA.png)

3) Faite “CTRL C” ou redémarrer la carte plusieurs jusqu'à avoir les chevrons ">>>"
4) Modifier le programme (Voir code Python) en changeant les informations suivantes :
- "Nom_point_accès","Mot_de_passe" 
- "votre_adresse_mail", "mot_de_passe_compte_maqiatto" 
- "votre_adresse_mail/nom_topic" 
- "votre_adresse_mail/nom_topic1"
Par votre mail et mot de passe enregistrer sur maqiatto ainsi que le nom de vos topic

5) Transférer le programme directement dans la carte en cliquant sur les fichiers de la carte et faisant transférer …(a revoir)
6) Placer la carte sur le rover
7) Allez sur Maqiatto.com et HVMQ suivez les instructions ("Voir les Pré-Requis")
8) Lancer le programme en allant dans les paramètres de la carte éxécuter le
9) Lancer l’application et connectez vous au serveur MQTT via l'interface
10) Amusez-Vous ;)

## Capture d'écran application (PREVIEW)  ##
![App Screenshot](https://cdn.discordapp.com/attachments/1003942960284573746/1023333535613997136/Param.PNG)

![App Screenshot](https://cdn.discordapp.com/attachments/1003942960284573746/1023333297260077066/infos.PNG)

![App Screenshot](https://cdn.discordapp.com/attachments/1003942960284573746/1023334073873223781/Aide.PNG)

![App Screenshot](https://cdn.discordapp.com/attachments/1003942960284573746/1023334074196181032/mqtt.PNG)

#
Créer avec Python, MIT App Inventor

Copyright © 2022 | Rover Control | Tous Droits Réservés.
