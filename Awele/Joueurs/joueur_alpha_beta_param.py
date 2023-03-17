#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game
import random

PROFONDEUR=1
COMPTEUR=0 
"""
#26 win
params_BEG = [0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
params_MID = [0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
params_END = [0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
"""

#param vs alpha beta prof.6 
params_BEG =[-0.99999999998, 0.99999999999, 0.99999999993, 0.0, 0.99999999991, 0.0, -0.99999999999, -0.99999999981, 0.99999999999]
params_MID = [-0.99999999999, 0.0, 0.0, -0.99999999986, -0.99999999993, 0.0, 0.0, 0.0, 0.99999999994]
params_END = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

params_TOT = params_BEG + params_MID + params_END

#[-0.99999999999, -2.000000165480742e-11, -0.99999999999, -8.600000711567191e-10, 0.0, 1.00000000046, 0.0, 0.0, 0.99999999999]
#params = [-0.99999999999, -2.000000165480742e-11, -0.99999999999, -8.600000711567191e-10, 0.0, 1.00000000046, 0.0, 0.0, 0.99999999999]
def saisieCoup(jeu):  

    """ jeu -> coup
        Retourne un coup a jouer    
    """
    return decision(jeu,game.getCoupsValides(jeu))

def decision(jeu,listCoup) :
    global PROFONDEUR , PLAYER, COMPTEUR
    PLAYER = jeu[1]
    scoreMax= -1000000000000
    l = []
    coupMax=listCoup[random.randint(0,len(listCoup)-1)]
    for i in range(0,len(listCoup)):                       
            score = estimation(jeu,listCoup[i],PROFONDEUR,scoreMax,100000000000)
            if ( score > scoreMax) : 
                scoreMax=score 
                coupMax=listCoup[i]
                l= []
            if (score == scoreMax):
                if coupMax not in l : 
                    l.append(coupMax)
                else : 
                    l.append(listCoup[i])
    #print("Noeuds visités : ",COMPTEUR)
    if l == [] : 
        return coupMax
    return l[random.randint(0,len(l)-1)]


def estimation(jeu,coup,profondeur,alpha,beta):
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
        return max_value(copie_jeu,profondeur,alpha,beta) # joueur 1 
    return min_value(copie_jeu,profondeur,alpha,beta)  # joueur 2 


def f1(jeu): #evaluation_nb_puits_sup11 (offensif)
    plateau=jeu[0]
    nb_puits= 0
    nb_capture = 0 
    if (PLAYER == 1) :
        for i in range (0,len(plateau)):
            if ((plateau[PLAYER%2][i]==1) or (plateau[PLAYER%2][i]==2)):
                nb_capture+=1
        if ((plateau[PLAYER-1][0] > 11) and nb_capture > 0):
            return 10
    else :
        for i in range (0,len(plateau)):
            if ((plateau[PLAYER%2][i]==1) or (plateau[PLAYER%2][i]==2)):
                nb_capture+=1
        if ((plateau[PLAYER-1][0] > 11) and nb_capture > 0):
            return 10
    return 0
    
def f2(jeu) : #evaluation_diff_score (offensif)
    if (PLAYER == 2):
        return jeu[4][PLAYER-1]-jeu[4][PLAYER-2]
    return jeu[4][PLAYER-1]-jeu[4][PLAYER]

def f3(jeu)  : # case à 0 , 1 ou 2 graine(s) dans le camp adverse  (offensif)
    plateau=jeu[0]
    adver = PLAYER%2
    res= 0
    for i in range(0,len(plateau[adver])):
        if(((plateau[adver][i] == 0 ) or (plateau[adver][i] == 1 ) or (plateau[adver][i] == 2))):
            res+=1
    return res+5 

def f4(jeu): # combo effectué  (offensif)
    plateau=jeu[0]
    adver = PLAYER%2+1#camp adverse 
    count = 0
    max_count = 0
    if (adver == 2 ):
        for i in range(0,len(plateau[adver-1])):
            if (plateau[adver-1][i] == 0):
                count=+1
            else  : 
                max_count = count
                count = 0
                  
        if max_count >= 2 :
            return 2**max_count
    else : 
        i = 5
        while (i > -1):
            if (plateau[adver-1][i] == 0):
                count=+1
            else  : 
                max_count = count
                count = 0
            i-=1
        if max_count >= 2 :
            return 2**max_count
    return 0

def f5(jeu): #mon camp sécurisé (defensif)
    plateau=jeu[0]
    camp = PLAYER-1
    res= 0
    for i in range(0,len(plateau[camp])):
        if((plateau[camp][i] == 1 ) or (plateau[camp][i] == 2) or (plateau[camp][i] == 0)):
            res+=1
    return (2**res)*(-1) 



def f6(jeu): # SCORE 
    return  jeu[4][PLAYER-1]

def f7(jeu) :  # Objectif de création d'un puit
    plateau=jeu[0]
    nb_puits= 0
    for i in range (0,len(plateau[0])) :
        if plateau[PLAYER-1][i] >= 6 :
            nb_puits+=1
    return nb_puits+5

def f8(jeu): #  objectif combo
    plateau=jeu[0]
    adver = PLAYER%2+1 #camp adverse 
    count = 0
    max_count = 0
    if (adver == 2 ):
        for i in range(0,len(plateau[adver-1])):
            if(((plateau[adver-1][i] == 1 ) or (plateau[adver-1][i] == 2))):
                count=+1
            else  : 
                max_count = count
                count = 0           
        if max_count >= 2 :
            return 2*max_count
    else : 
        i = 5
        while (i > -1):
            if(((plateau[adver-1][i] == 1 ) or (plateau[adver-1][i] == 2))):
                count=+1
            else  : 
                max_count = count
                count = 0
            i-=1
        if max_count >= 2 :
            return 2*max_count
    return 0

def f9(jeu) : #diff nb_graine
    plateau=jeu[0] 
    nb_graine1 = 0
    nb_graine2 = 0
    for i in range(0,len(plateau[PLAYER-1])):
        nb_graine1+=plateau[PLAYER-1][i]
        nb_graine2+=plateau[PLAYER%2][i]
    return nb_graine1-nb_graine2

def evaluation(jeu) : 
    s = scores(jeu)

    if (len(jeu[3]) < 20 ) : 
        return dot(params_BEG,s)
    if (len(jeu[3]) >= 20 and  len(jeu[3]) < 60 ) :
        return dot(params_MID,s)
    else : 
        return dot(params_END,s)
    
   # return dot(params,s)

def dot(v1,v2):
    return sum([v1[i]*v2[i] for i in range(0,len(v1))])


def scores(jeu) : 
    global f1 ,f2 ,f3,f4,f5,f6,f7,f8,f9
    return [f1(jeu),f2(jeu),f3(jeu),f4(jeu),f5(jeu),f6(jeu),f7(jeu),f8(jeu),f9(jeu)]

def addparam(i,k):
    
    global params_BEG , params_MID , params_END , params_TOT
    params_TOT[i] = params_TOT[i] + k

    if i < 9 : 
        params_BEG[i]=params_BEG[i]+k
    elif i>=9 and i<18 :
        params_MID[i%9] = (params_MID[i%9]+k)
    else : 
        params_END[i%9] = (params_END[i%9]+k)
    
    #params[i] = params[i] + k 
def max_value(jeu,profondeur,alpha,beta):
    m = alpha
    for c in game.getCoupsValides(jeu):
        alpha = m
        if ( m >= beta):
            return m
        m = max(estimation(jeu,c,profondeur-1,alpha,beta), m)
    return m

def min_value(jeu,profondeur,alpha,beta):
    m = beta
    for c in game.getCoupsValides(jeu):
        m = min(estimation(jeu,c,profondeur-1,alpha,beta), m)
        beta = m 
        if( m <= alpha ):
            return m-1   # car c'est une égalité avec alpha 
    return m

