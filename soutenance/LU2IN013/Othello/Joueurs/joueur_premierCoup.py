#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    return decision(jeu,game.getCoupsValides(jeu))

def decision(jeu,listCoup) :
    return listCoup[0]

