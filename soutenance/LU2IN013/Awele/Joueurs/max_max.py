#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game

PROFONDEUR=2

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    return decision(jeu,game.getCoupsValides(jeu))

def decision(jeu,listCoup) :
    global PROFONDEUR
    scoreMax= -100
    coupMax = listCoup[0] 
    for i in range(0,len(listCoup)):
            score = estimation(jeu,listCoup[i],PROFONDEUR,jeu[1])
           # print("score :",score," Coup : ",listCoup[i],"\n")
            if (score > scoreMax) : 
                scoreMax=score 
                coupMax=listCoup[i]
    PROFONDEUR+=1
    return coupMax


def estimation(jeu,coup,profondeur,joueur):
    copie_jeu=game.getCopieJeu(jeu)
    game.joueCoup(copie_jeu,coup)

    if  profondeur ==  0 :
        return evaluation_score(copie_jeu) 
    if (jeu[1] == joueur ): 
        return estimation(copie_jeu,meilleur_coups(jeu),profondeur-1,joueur) 
    return estimation(copie_jeu,pire_coups(jeu),profondeur-1,joueur) 

def evaluation_score(jeu):

    return  jeu[4][jeu[1]-1]

def calcul_score(jeu) :
    if (jeu[1] == 2 ):
        return (game.getScore(jeu,1)-game.getScore(jeu,2))
    return (game.getScore(jeu,2)-game.getScore(jeu,1))


def pire_coups(jeu) : 
    """ Retourne le pire coups possible 
                                    """
    pire_score=100
    pire_coups = [-1,-1]
    for i in game.getCoupsValides(jeu) :
        copie_jeu=game.getCopieJeu(jeu)
        game.joueCoup(copie_jeu,i)
        game.changeJoueur(jeu)
        score = calcul_score(copie_jeu)
        if score < pire_score : 
            pire_score = score 
            pire_coups = i 
    return  pire_coups


def meilleur_coups(jeu) : 
    """ Retourne le meilleur coups possible 
                                """
    meilleur_score= - 100
    meilleur_coups = [-1,-1]
    for i in game.getCoupsValides(jeu) :
        copie_jeu=game.getCopieJeu(jeu)
        game.joueCoup(copie_jeu,i)
        game.changeJoueur(jeu)
        score = calcul_score(copie_jeu)
        if score > meilleur_score : 
            meilleur_score = score 
            meilleur_coups = i 
    return  meilleur_coups
