#!/usr/bin/python
# -*- coding: utf-8 -*-

from config import Config
from color import Color
from acquisition import acquisition
import sys
import os

threshold = 0.05
if len(sys.argv) > 1 :
	threshold = float(sys.argv[1])

firstCfg  = Config("First")
secondCfg = Config("Second")

### Display title
print
print "\t\t\t\tProgramme" + Color.BOLD + " MAGELLI" + Color.NORMAL

### ETAPE 1: apprentissage sur un court texte
print
print "-"*70
print Color.BOLD + "Entrez un texte de votre choix et terminez en tapant deux fois Entrée :" + Color.NORMAL
freq_bs = acquisition(firstCfg)
print Color.CYAN + "Fréquence des BACKSPACE: " + str(freq_bs) + Color.NORMAL
print "-"*70

### ETAPE 2: écriture d'un deuxième texte (identique ou non)
print Color.BOLD + "Entrez un deuxième texte (identique ou non) et terminez en tapant deux fois Entrée :" + Color.NORMAL
freq_bs = acquisition(secondCfg)
print Color.CYAN + "Fréquence des BACKSPACE: " + str(freq_bs) + Color.NORMAL
print "-"*70
print

### ETAPE 3: comparaison des deux (sensibilité variable)
inter = firstCfg.intersection(secondCfg)
sum = 0
i   = 0

# calcul de la somme des différences de temps
for item in inter :
	absolute = abs(secondCfg.dict[str(item)].val - firstCfg.dict[str(item)].val)
	count = secondCfg.dict[str(item)].it + firstCfg.dict[str(item)].it
	sum += absolute*count
	i += count
	
# calcul de la moyenne des différences de temps
if i != 0 :
	sum /= i
print Color.BOLD + "Différence moyenne : " + str(sum) + " s" + Color.NORMAL
print Color.BOLD + "Effectué avec " + str(len(inter)) + " combinaisons, soit " + str(i) + " données" + Color.NORMAL
print Color.BOLD + "Seuil de comparaison : " + str(threshold) + Color.NORMAL
print

# sauvegarde des données pour afficher les graphes
mon_fichier = open("diff.csv","w")
mon_fichier2 = open("diff2.csv","w")
for item in inter:
	di = abs(secondCfg.dict[str(item)].val - firstCfg.dict[str(item)].val)
	mon_fichier.write(str(secondCfg.dict[str(item)].val)+", "+str(firstCfg.dict[str(item)].val)+"\n")
	mon_fichier2.write(str(di)+"\n")
mon_fichier.close()

# interprétation du seuil
if sum < threshold and len(inter) > 0 :
	print Color.BLUE + "Le programme juge qu'une seule personne a saisi les deux textes =)" + Color.NORMAL
elif len(inter) > 0 :
	print Color.RED + "Le programme juge que deux personnes ont saisi les deux textes =(" + Color.NORMAL
else :
	print Color.PURPLE + "Le programme ne dispose pas d'assez de données ö_o" + Color.NORMAL
print
