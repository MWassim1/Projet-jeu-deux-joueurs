#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game
import random

PROFONDEUR=4
COMPTEUR=0 


def saisieCoup(jeu):  
    """ jeu -> coup
        Retourne un coup a jouer    
    """
    return decision(jeu,game.getCoupsValides(jeu))

def decision(jeu,listCoup) :
    global PROFONDEUR , PLAYER, COMPTEUR
    PLAYER = jeu[1]
    scoreMax= -100000
    l = []
    coupMax=listCoup[random.randint(0,len(listCoup)-1)]
    for i in range(0,len(listCoup)):                       
            score = estimation(jeu,listCoup[i],PROFONDEUR)
            if ( score > scoreMax) : 
                scoreMax=score 
                coupMax=listCoup[i]
                l= []
            if (score == scoreMax):
                if coupMax not in l : 
                    l.append(coupMax)
                else : 
                    l.append(listCoup[i])
    print("Noeuds visités : ",COMPTEUR)
    if l == [] : 
        return coupMax
    return l[random.randint(0,len(l)-1)]


def estimation(jeu,coup,profondeur):
    copie_jeu=game.getCopieJeu(jeu)
    game.joueCoup(copie_jeu,coup)
    if (game.finJeu(copie_jeu)): 
        if (game.getGagnant(copie_jeu) == PLAYER) :
            return 10000000000
        if (game.getGagnant(copie_jeu) == 0 ) :
            return  -1000
        if (game.getGagnant(copie_jeu) == PLAYER%2+1) :
            return -10000000000
    if  profondeur ==  1 :
        return evaluation(copie_jeu)
    if (copie_jeu[1] == PLAYER ): 
        return max_value(copie_jeu,profondeur) # joueur 1 
    return min_value(copie_jeu,profondeur)  # joueur 2 


def f1(jeu): #evaluation score 
    return  jeu[4][PLAYER-1]


def f2(jeu): #evaluation bords + coins (offensif)
    plateau = jeu[0]
    res = 0
    for i in range(0,len(plateau)):
        if (plateau[0][i] == PLAYER):
            if(i == 0) :  # (0,0)
                res+=10
            if (i == len(plateau)-1):  # (0,8)
                res+=10
            res+=1
        if (plateau[len(plateau)-1][i] == PLAYER):
            if(i ==0) : #(8,0)
                res+=10
            if(i == len(plateau)-1): #(8,8)
                res+=10
            res+=1
        if (plateau[i][0] == PLAYER):
            res+=1
        if (plateau[i][len(plateau)-1]== PLAYER):
            res+=1
    return res 

def f3(jeu): #evaluation bords + coins (defensif)
    plateau = jeu[0]
    res = 0
    for i in range(0,len(plateau)):
        if (plateau[0][i] == PLAYER%2+1):
            if(i == 0) :  # (0,0)
                res+=10
            if (i == len(plateau)-1):  # (0,8)
                res+=10
            res+=1
        if (plateau[len(plateau)-1][i] == PLAYER%2+1):
            if(i ==0) : #(8,0)
                res+=10
            if(i == len(plateau)-1): #(8,8)
                res+=10
            res+=1
        if (plateau[i][0] == PLAYER%2+1):
            res+=1
        if (plateau[i][len(plateau)-1]== PLAYER%2+1):
            res+=1
    return res*(-1)
def f4(jeu) : # empêche de jouer angles (defensif)
    plateau = jeu[0]
    res = 0 
    #Protection angle haut - gauche 
    if (plateau[0][1] == PLAYER) : 
        res+=1
    if (plateau[1][1]== PLAYER):
        res+=5   # très dangereuse 
    if (plateau[1][0]== PLAYER):
        res+=1

    #Protection angle haut-droit 
    if (plateau[0][6]== PLAYER):
        res+=1
    if (plateau[1][6]== PLAYER):
        res+=5
    if (plateau[1][7]== PLAYER):
        res+=1
    
    #Protection angle bas - gauche 
    if (plateau[7][1]== PLAYER):
        res+=1
    if (plateau[6][1]== PLAYER):
        res+=5
    if (plateau[6][0]== PLAYER):
        res+=1
    
    #Protection angle bas - droite 
    if (plateau[7][6]== PLAYER):
        res+=1
    if (plateau[6][6]== PLAYER):
        res+=5
    if (plateau[6][7]== PLAYER):
        res+=1

    return res *(-1)
def f5(jeu) : #différence  de pions (offensif) - objectif avoir le moins de pions que possible afin d'avoir plus de coups disponibles  
    plateau = jeu[0]
    nb_pionsJ1 = 0
    nb_pionsJ2 = 0
    for i in range(0,len(plateau)):
        for j in range(0,len(plateau)):
            if (plateau[i][j]==1):
                nb_pionsJ1+=1
            if (plateau[i][j]== 2 ):
                nb_pionsJ2+=1
    if (nb_pionsJ2 > nb_pionsJ1): 
        return 10
    if (nb_pionsJ1 > nb_pionsJ2) : 
        return -15
    return 0


def evaluation(jeu):
    global COMPTEUR
    COMPTEUR+=1
    return f1(jeu)+f2(jeu)+f3(jeu)+f4(jeu)+f5(jeu)

def max_value(jeu,profondeur):
    m = -1000
    for c in game.getCoupsValides(jeu):
        m = max(estimation(jeu,c,profondeur-1), m)
    return m

def min_value(jeu,profondeur):
    m= 1000
    for c in game.getCoupsValides(jeu):
        m = min(estimation(jeu,c,profondeur-1), m)
    return m


