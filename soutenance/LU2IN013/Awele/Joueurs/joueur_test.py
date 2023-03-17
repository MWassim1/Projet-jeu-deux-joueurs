#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game
sys.path.append("./Joueurs")




def evaluation_score(jeu):
    return  jeu[4][PLAYER-1]

def evaluation_nb_puits_sup11(jeu):
    plateau=jeu[0]
    nb_puits= 0
    for i in range (0,len(plateau[0])) :
        if plateau[PLAYER-1][i] > 11 :
            nb_puits+=1
    return nb_puits
    
def evaluation_diff_score(jeu) :
    if (jeu[1] == 1 ) : 
        return jeu[4][0] - jeu[4][1]
    return jeu[4][1] - jeu[4][0]

f1=evaluation_score
f2=evaluation_nb_puits_sup11
f3 =evaluation_diff_score


global params 
params = [0,0,0]

def saisieCoup(jeu):  
    """ jeu -> coup
        Retourne un coup a jouer    
    """
    return evaluation(jeu)

def evaluation(jeu) : 
    global PLAYER 
    PLAYER = jeu[1]
    s = scores(jeu)
    return dot(params,s)

def dot(v1,v2):
    return sum([v1[i]*v2[i] for i in range(0,len(v1))])

def scores(jeu) : 
    return [f1(jeu),f2(jeu),f3(jeu)]

def addparam(i,k):
    return i+k