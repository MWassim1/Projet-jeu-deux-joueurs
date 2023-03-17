#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
game.joueur1=min_max
game.joueur2=joueur_Alea
"""
jeu=game.initialiseJeu()
game.affiche(jeu)
game.joueCoup(jeu,[0,1])
game.affiche(jeu)
game.joueCoup(jeu,[1,2])
game.affiche(jeu)
print(game.joueur1.saisieCoup(jeu))
"""
"""
jeu2=game.getCopieJeu(jeu)
game.joueCoup(jeu2,[1,2])
game.affiche(jeu2)
game.affiche(jeu)
print(jeu[3],"\n",jeu2[3])
print(jeu[1],"\n",jeu2[1])
"""


def partie1(affiche,alea,prop_part):
	"""
		Lance 1 partie avec un affichage du plateau 
		2 Joueurs humain 
												"""	
	nb_tours=1
	jeu=game.initialiseJeu()
	if prop_part > 0.5:
		game.changeJoueur(jeu)
	
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


def stats(j1,j2,eg):
	win_j1 = 0 
	win_j2 = 0 
	e = 0 
	n_game=100
	for i in range (0,n_game):
		winner = partie1(False,True,i/n_game)
		if (winner== 1):
			win_j1+=1
		elif (winner== 2): 
			win_j2+=1
		else : 
			e+=1
	j1.append(win_j1)
	j2.append(win_j2)
	eg.append(e)
	print("Player 1 -> ",win_j1,"  Player 2 ->",win_j2)

def partie(n_rounds):
	t_res = [] ; j1 = [] ; j2 = [] ; eg = []
	res_j1 = 0 ; res_j2 = 0 ; res_eg= 0
	for i in range (0,n_rounds):
		print("Round ",i," :")
		stats(j1,j2,eg)
	for i in range(0,n_rounds):
		res_j1+=j1[i]
		res_j2+=j2[i]
		res_eg+=eg[i]
	print("\nPlayer 1 : ",res_j1/10,"% ")
	print("Player 2 : ",res_j2/10,"% ")	 
	print("Draw : ",res_eg/10,"%\n")


#print("Le gagnant est le joueur :",partie1(True,True,0))
#stats([],[],[])
partie(10)
