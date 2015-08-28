#!/usr/bin/python
# -*- coding: utf-8 -*-

from getch import _Getch
from timer import Timer
import sys

def acquisition(config) :
	
	timer      = Timer()
	getch	   = _Getch()
	last_char  = ""
	last_char2 = ""
	nl_count   = 0
	bs_count   = 0
	char_count = 0
	quit       = False
	
	while(not quit) :
		# on lit un caractère
		my_char = getch()
		char_count += 1
		# saut de ligne:
		if my_char == "\r":
			print
			nl_count += 1
			# reset le dernier caractère
			last_char  = ""
			last_char2 = ""
		# autre caractère
		else:
			nl_count = 0
			# caractère BACKSPACE
			if my_char == '\x08' or my_char == '\x7f':
				# on compte le nb de backspace pour les stats
				bs_count += 1
				# écrire un backspace déplace simplement le curseur
				# il faut effacer avec un espace
				sys.stdout.write("\x08 \x08")
				# reset le dernier caractère
				last_char = ""
			else:
				sys.stdout.write(my_char)
				
				# si un précédent caractère était présent
				if last_char != "" :
					# récupérer le temps entre deux frappes
					t = timer.time()

					# ajout dans la configuration si l'intervalle semble correct
					if t < 1 :
						config.add(last_char + my_char, t)
				
					if last_char2 != "" :
						config.add(last_char2 + last_char + my_char, t)
				# sauvegarde du dernier caractère
				last_char2 = last_char
				last_char  = my_char

		# deux appuis simultanés sur ENTER quittent la boucle 
		if nl_count == 2:
			quit = True

		# reset du chronomètre
		timer.start()

	return float(bs_count) / float(char_count) * 100
