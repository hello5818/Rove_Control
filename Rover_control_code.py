from m5stack import *     # Importe un module
from m5mqtt import M5mqtt #
from m5ui import *        #
from uiflow import *      #
import wifiCfg            #
import time               #
import hat                #

#------------- Partie Robot, Déplacement -------------#
hat_roverc1 = hat.get(hat.ROVERC)
def receptionData(topic_data): # Fonction qui deplace le robot
    lcd.print('recu='+str(topic_data)+'', 0, 10)
    if str(topic_data) == 'avance': # Fait avancer le robot
        hat_roverc1.SetSpeed(0, 40, 0)  ## Gère la vitesse des roues
        wait(1) ### Attend 1 seconde
        hat_roverc1.SetSpeed(0, 0, 0)   ##
    if str(topic_data) == 'recule': # Fait reculer le robot
        hat_roverc1.SetSpeed(0, -40, 0) ##
        wait(1) ###
        hat_roverc1.SetSpeed(0, 0, 0)   
    if str(topic_data) == 'gauche':
        hat_roverc1.SetSpeed(-40, 0, 0) 
        wait(1)
        hat_roverc1.SetSpeed(0, 0, 0)
    if str(topic_data) == 'droite':
        hat_roverc1.SetSpeed(0, 0, +40) 
        wait(1)
        hat_roverc1.SetSpeed(0, 0, 0)
    if str(topic_data) == 'son':
         speaker.tone(2000, 50)
         speaker.tone(1500, 1000) # Hauteur du son + temmps en ms
         speaker.tone(2000, 100)
         speaker.tone(1500, 50)                
#------------- Partie MQTT -------------#
wifiCfg.doConnect("Nom_point_accès","Mot_de_passe") # !!! Point d'acceset mot de passe a changer !!!
m5mqtt = M5mqtt('test1', 'maqiatto.com', 1883, 'votre_adresse_mail', 'mot_de_passe_maqiatto', 10000) # Paramétrage du MQTT avec le mot de passe, l'adresse mail, le port ....
m5mqtt.subscribe('votre_adresse_mail/nom_topic1', receptionData) # Reçoit les données
m5mqtt.start() # Lance m5qtt
value = 0 # Variable
lcd.print('connected',0,20) # Affiche un message sur la M5 (Message : Connecté !)
m5mqtt.publish('votre_adresse_mail/nom_topic',"start") # Information publié
'''while True :
      time.sleep_ms(2000)
      value=10+(value+1)%15
      lcd.print("Valeur = "+str(value), 0, 30)
      m5mqtt.publish('votre_adresse_mail/nom_topic',str(value)+" degres")'''
#-----------------------------------------------------------------------------------#
