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
import joueur_alpha_beta_param
joueur=joueur_alpha_beta_param

liste_adversaire = [joueur_alpha_beta]#,joueur_alpha_beta,joueur_debut]

def partie1(affiche,alea):
	"""
		Lance 1 partie avec un affichage du plateau 
		2 Joueurs humain 
												"""	
	
	nb_tours=1
	jeu=game.initialiseJeu()
	while( not game.finJeu(jeu) and  nb_tours <= 100):
		if (alea and nb_tours<=4): 
			coup=joueur_Alea.saisieCoup(jeu)
			game.joueCoup(jeu,coup)
		else :
			coup=game.saisieCoup(jeu)
			game.joueCoup(jeu,coup)
		if(affiche):
			game.affiche(jeu)
		nb_tours+=1
	#game.affiche(jeu)
	return game.getGagnant(jeu)


def stats(j1,j2,first):
    game.joueur1=j1
    game.joueur2=j2
    win_j1 = 0
    win_j2 = 0 
    n_game=50
    if(first == True):
    	for i in range (0,n_game):
    		winner = partie1(False,True)
    		if (winner== 1):
    			win_j1+=1
    	return win_j1
    else : 
    	for i in range (0,n_game):
    		winner = partie1(False,True)
    		if (winner== 2):
    			win_j2+=1
    return win_j2
	
def train():
	E = 1 
	nb_tours = 1
	oldparam = stats(joueur,liste_adversaire[random.randint(0,len(liste_adversaire)-1)],True)
	while nb_tours < 1001: 
		E = E * 0.99999999999
		for i in range(0,len(joueur.params_TOT)) : 
			
			rand = int(random.random()*100)
			if (random.random() < 0.50):
				s = -1 
			else :
				s = 1
			joueur.addparam(i,E*s)
			sc = stats(joueur,liste_adversaire[random.randint(0,len(liste_adversaire)-1)],True) 
			sc += stats(liste_adversaire[random.randint(0,len(liste_adversaire)-1)],joueur,False)
			if sc < oldparam : 
				joueur.addparam(i,-E*s) 
			else:
				oldparam = sc
			#print(nb_tours,E,oldparam,sc,joueur.params_BEG,joueur.params_MID,joueur.params_END)
			#print(nb_tours,oldparam,joueur.params_BEG,joueur.params_MID,joueur.params_END)
			print(nb_tours,oldparam)
			nb_tours +=1
train()
