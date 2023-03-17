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
        l=int(input("Saisie la ligne : "))
        c=int(input("Saisie de la colonne: "))
    except :
        l=-1
        c=-1
        pass 
    while( not game.coupValide(jeu,[l,c])):
        print("Coup non valide : ")
        try : 
            l=int(input("Saisie la ligne : "))
            c=int(input("Saisie de la colonne: "))
        except : 
            continue
    return [l,c]
