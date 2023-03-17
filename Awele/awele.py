#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ast import increment_lineno
from readline import insert_text


def initialisePlateau() : 
    plateau = []
    for i in range (0,2) :
        liste = [4,4,4,4,4,4]
        plateau.append(liste)
    return plateau
def initialiseScore() : 
    return [0,0]

def copie_score(jeu) : 
    score=jeu[4]
    copie_score=[]
    for i in score:
        copie_score.append(i)
    return copie_score

def estAffame(jeu,joueur):
    if (joueur == 1 ) : 
        return sum(jeu[0][joueur]) == 0
    return sum(jeu[0][joueur-2]) == 0


def finalisePartie(jeu) : 
    plateau = jeu[0]
    for i in range(0,6):
        jeu[4][1]+=plateau[1][i]
    for i in range(0,6):
        jeu[4][0]+=plateau[0][i]


def listeCoupsValides(jeu) : 
    listCoups = []
    plateau = jeu[0]
    for i in range (0,len(plateau)) :
        for j in range (0,len(plateau[i])):
            if(estValide(jeu,[i,j]) and (jeu[1]-1 == i)):
                listCoups.append([i,j])
    return listCoups


def estValide(jeu,coup):
    plateau=jeu[0]
    if (coup[0]==0):
        return plateau[coup[0]][coup[1]] > coup[1]
    if (coup[0] == 1) : 
        return (plateau[coup[0]][coup[1]] > (5-coup[1])) 
    



def copie_plateau(jeu) : 
    plateau = jeu[0]
    copie_plateau = []
    liste = []
    for i in range (0,len(plateau)):
        for j in range (0,len(plateau[i])):
            liste.append(plateau[i][j])
        copie_plateau.append(liste)
        liste=[]
    return copie_plateau

def saisieCoup(jeu,coup): 
    jeu[3].append(coup)
    plateau=jeu[0]
    plateau_initial = copie_plateau(jeu)
    liste = []
    nb_graine=plateau[coup[0]][coup[1]]
    graine_dep = nb_graine

    joueur = jeu[1]
    """ On met la case du coup joué à 0
                                    """
    plateau[coup[0]][coup[1]] = 0

    """ On égraine nb_graine dans le plateau
    
                                       """
    l=coup[0]; c=coup[1]+1
    if (l==1):
        increment = True 
        c=coup[1]+1
    else :
        increment = False
        c=coup[1]-1
    while (nb_graine > 0):
        if (c == 6) :
            c=5 ; l=0
            jeu[0] = plateau
            plateau=copie_plateau(jeu)
            increment = False 
        if ( c == -1 ) : 
            c = 0 ; l=1
            jeu[0] = plateau
            plateau=copie_plateau(jeu)
            increment = True
        if([l,c] != [coup[0],coup[1]]): # Vérifie si on fait un tour complet (le cas où le coup joué donne plus de 12 graines )
            nb_graine-=1
            plateau[l][c]+=1
        if (nb_graine == 0):
            break
        #Sens anti-horaire si increment == True , horaire sinon
        if(increment):
            c+=1
        else:
            c-=1   
    if (c == 6) :
        c=5 
    if ( c == -1): 
        c = 0  
    # On ramasse les graines 
    score =  copie_score(jeu)
    if((graine_dep <= 11 - c ) or (plateau[l][c]==2 or plateau[l][c]==3)): 
        while((plateau[l][c]==2 or plateau[l][c]==3)) : 
                if(l == 1 and jeu[1] == 1) : 
                    score[0]+=plateau[l][c]
                    plateau[l][c] = 0
                if (l == 0 and jeu[1] == 2 ) : 
                    score[1]+=plateau[l][c]
                    plateau[l][c] = 0
                if(increment ) : 
                    c-=1
                if (not increment) : 
                    c+=1
                if ((c < 0) or (c >5)) : 
                    break
        copie_jeu = [] ; copie_jeu.append(plateau)
        if (estAffame(copie_jeu,jeu[1])== False ):
            jeu[0] = plateau
            jeu[4] = score
        else :
            jeu[0] = plateau_initial
    else :
        jeu[0] = plateau    
    jeu[2] = None
    jeu[1] = jeu[1]%2+1 