from m5stack import *     # Importe un module
from m5mqtt import M5mqtt #
from m5ui import *        #
from uiflow import *      #
import wifiCfg            #
import time               #
import hat                #


#--------------- Son / Musique ------------------#
    # Variable avec les tonalités et les notes du son
freq = { "cL":129, "cLS":139, "dL":146, "dLS":156, "eL":163, "fL":173, "fLS":185, "gL":194, "gLS":207, "aL":219, "aLS":228, "bL":232, "c":261, "cS":277, "d":294, "dS":311, "e":329, "f":349, "fS":370, "g":391, "gS":415, "a":440, "aS":455, "b":466, "cH":523, "cHS":554, "dH":587, "dHS":622, "eH":659, "fH":698, "fHS":740, "gH":784, "gHS":830, "aH":880, "aHS":910, "bH":933, "R":200000 }
#  CS = do # C
# Star Wars 
music =  [ ["a",500], ["a",500], ["f",350], ["cH",150], ["a",500], ["f",350], ["cH",150], ["a",1000], ["eH",500], ["eH",500], ["eH",500], ["fH",350], ["cH",150], ["gS",500], ["f",350], ["cH",150], ["a",1000], ["aH",500], ["a",350], ["a",150], ["aH",500], ["gHS",250], ["gH",250], ["fHS",125], ["fH",125], ["fHS",250], ["R",250], ["aS",250], ["dHS",500], ["dH",250], ["cHS",250], ["cH",125], ["b",125], ["cH",250], ["R",250], ["f",125], ["gS",500], ["f",375], ["a",125], ["cH",500], ["a",375], ["cH",125], ["eH",1000], ["aH",500], ["a",350], ["a",150], ["aH",500], ["gHS",250], ["gH",250], ["fHS",125], ["fH",125], ["fHS",250], ["R",250], ["aS",250], ["dHS",500], ["dH",250], ["cHS",250], ["cH",125], ["b",125], ["cH",250], ["R",250], ["f",250], ["gS",500], ["f",375], ["cH",125], ["a",500], ["f",375], ["c",125], ["a",1000] ]
# Tetris #
#music =[["eH",400],["b",200],["cH",200],["dH",400],["cH",200],["b",200],["a",400],["a",200],["cH",200],["eH",400],["dH",200],["cH",200],["b",400],["b",200],["cH",200],["dH",400],["eH",400],["cH",400],["a",400],["a",400]]
#---Fin Tetris--#
tab_music_final = []
for note in music :
   tab_music_final.append(note)
   tab_music_final.append(["R",100])
music = tab_music_final
# Infos : A = La B = Si  C = Do  D = Ré E= Mi  F= Fa  G = Sol
   
#---------------------------------------------------#


#------------- Partie Robot, Déplacement -------------#
hat_roverc1 = hat.get(hat.ROVERC)
def receptionData(topic_data): # Fonction qui deplace le robot
    lcd.print('recu='+str(topic_data)+'', 0, 10)
  
    if str(topic_data) == 'avance': # Fait avancer le robot
        hat_roverc1.SetSpeed(0, 100, 0)  ## Gère la vitesse des roues
        wait(1) ###
        hat_roverc1.SetSpeed(0, 0, 0)   #X,Y,R
    if str(topic_data) == 'recule': # Fait reculer le robot
        hat_roverc1.SetSpeed(0, -100, 0) ##
        wait(1) ###
        hat_roverc1.SetSpeed(0, 0, 0)   #X,Y,R
    if str(topic_data) == 'gauche':
        hat_roverc1.SetSpeed(100, 0, 0) 
        wait(1)
        hat_roverc1.SetSpeed(0, 0, 0)
    if str(topic_data) == 'droite':
        hat_roverc1.SetSpeed(-100, 0, 0) 
        wait(1)
        hat_roverc1.SetSpeed(0, 0, 0)
    if str(topic_data) == 'droite_legerement':
        hat_roverc1.SetSpeed(-20, 30, 0)   
        wait(1)
        hat_roverc1.SetSpeed(0, 0, 0)        
    if str(topic_data) == 'tourne_droite_gauche':
        hat_roverc1.SetSpeed(-20, -30, 0)  
        wait(1)
        hat_roverc1.SetSpeed(0, 0, 0)
    if str(topic_data) == 'avance_gauche':
        hat_roverc1.SetSpeed(20, 20, 0) 
        wait(1)
        hat_roverc1.SetSpeed(0, 0, 0)
    if str(topic_data) == 'avancer_gauche_bas':
        hat_roverc1.SetSpeed(20, -30, 0)
        wait(1)
        hat_roverc1.SetSpeed(0, 0, 0)
    if str(topic_data) == 'boost':
        hat_roverc1.SetSpeed(0, 255, 0)
    if str(topic_data) == 'rotation':
        hat_roverc1.SetSpeed(0, 0, 90) 
     
    if str(topic_data) == 'son':
         speaker.setVolume(50)
         for i in range(len(music)): # Fonction qui joue les notes à la suite afin de créer une mélodie
              speaker.tone( freq[music[i][0]], music[i][1]) # Joue la musique

                   
#------------- Partie MQTT -------------#
wifiCfg.doConnect("Nom_point_accès","Mot_de_passe")   # !!! Point d'acceset mot de passe a changer !!!
m5mqtt = M5mqtt('test1', 'maqiatto.com', 1883, 'votre_adresse_mail', 'mot_de_passe_maqiatto', 10000) # Paramétrage du MQTT avec le mot de passe, l'adresse mail, le port ....
m5mqtt.subscribe('votre_adresse_mail/nom_topic', receptionData) # Reçoit les données
m5mqtt.start() # Lance m5qtt
value = 0 # Variable
lcd.print('connected',0,20) # Affiche un message sur la M5 (Message : Connecté !)
m5mqtt.publish('votre_adresse_mail/nom_topic1',"start") # Information publié
#-----------------------------------------------------------------------------------#

