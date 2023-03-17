#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    try :
        c=int(input("Saisie la colonne : "))
    except :
        c=-1
        pass 
    while( not game.coupValide(jeu,[jeu[1]-1,c])):
        print("Coup non valide : ")
        try : 
            c=int(input("Saisie la colonne : "))
        except : 
            continue
    return [jeu[1]-1,c]
