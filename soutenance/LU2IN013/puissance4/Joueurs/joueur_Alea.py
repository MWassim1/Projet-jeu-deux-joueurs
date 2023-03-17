#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game
import random

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    return decision(jeu,game.getCoupsValides(jeu))

def decision(jeu,listCoup) :
 
    return listCoup[random.randint(0,len(listCoup)-1)]
