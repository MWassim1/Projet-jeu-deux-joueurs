#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import awele
import sys
sys.path.append("..")
import game
game.game=awele
sys.path.append("./Joueurs")
import joueur_humain
import min_max
import joueur_alpha_beta
import joueur_Alea
import joueur_debut
import joueur_alpha_beta_param_oracle
import joueur_alpha_beta_oracle
Oracle = joueur_alpha_beta_oracle
joueur=joueur_alpha_beta_param_oracle
joueur2 = joueur_alpha_beta

liste_adversaire = [joueur_alpha_beta]#,joueur_alpha_beta,joueur_debut]


def train():
	""" 1 round = 100 games 
					"""
	E = 1 
	nb_round = 1  
	max_win= 0
	while True:
		E = E * 0.99999999999
		
		"""if(nb_round %2 == 0):
			game.joueur1=joueur
			game.joueur2=joueur_alpha_beta
			p = 1 
		else : 
			game.joueur1=joueur_alpha_beta
			game.joueur2=joueur
			p = 2
		"""
		nb_game=1
		win = 0
		loose = 0
		while(nb_game < 100):
			jeu=game.initialiseJeu()
			game.joueur1=joueur
			game.joueur2=joueur_alpha_beta
			nb_tours = 1
			while( not game.finJeu(jeu) and  nb_tours <= 100):
				if (nb_tours<=4): 
					coup=joueur_Alea.saisieCoup(jeu)
					game.joueCoup(jeu,coup)
				else :
					liste_score_oracle=Oracle.saisieCoup(jeu)
					opt = 0
					score_max = liste_score_oracle[0]
					for i in  range (1,len(liste_score_oracle)):
						if liste_score_oracle[i] > score_max : 
							score_max = liste_score_oracle[i]
							opt = i
					o = joueur.params[opt]*joueur.evaluation(jeu,True)[opt]
					for c in range (0,len(game.getCoupsValides(jeu))):
						if c != opt :
							s = joueur.params[c]*joueur.evaluation(jeu,True)[c]
							#print("s : ",s," o : ",o)
							if o - s < 1 :
								for j in range (1,len(joueur.params)):
									joueur.params[j] = joueur.params[j]- E * (s-o)
					coup=game.saisieCoup(jeu)
					game.joueCoup(jeu,coup)
				nb_tours+=1
			nb_game+=1
			if(game.getGagnant(jeu) == 1):
				win+=1
			if(game.getGagnant(jeu) == 2):
				loose+=1
			"""
			if((p==2) and (game.getGagnant(jeu)==2)): 
				win+=1
			if((p==2) and (game.getGagnant(jeu) == 1)):
				loose+=1
			"""
		if(win > max_win):
			max_win=win
		print(nb_round,max_win,win,loose,joueur.params,nb_game)
		nb_round+=1
train()
