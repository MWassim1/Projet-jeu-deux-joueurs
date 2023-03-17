#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ast import increment_lineno
from readline import insert_text




def initialisePlateau():
    plateau = []
    for i in range(0,6):
        liste = [' ',' ',' ',' ',' ',' ',' ']
        plateau.append(liste)
    return plateau

def initialiseScore():
    return [0,0]

def listeCoupsValides(jeu):
    listCoups = []
    plateau = jeu[0]
    for i  in range(5,-1,-1):
        for j in range(0,7):
            if ((plateau[i][j] == ' ') and (i==5)):
                listCoups.append([i,j])
            elif( (plateau[i][j]  == ' ') and (i < 5) and (plateau[i+1][j] != ' ')):
                listCoups.append([i,j])
    print(listCoups)
    return listCoups

def maj_score(jeu,coup,score):
    plateau=jeu[0]
    cpt = 0
    player=plateau[coup[0]][coup[1]]
    for i in range (coup[0],len(plateau[coup[0]])):# on regarde à droite de la case jouée 
        if( (coup[1]+i < len(plateau[coup[0]])) and (plateau[coup[0]][coup[1]+i]) == player): 
            cpt+=1
            if (cpt >= 4 ):
                if(jeu[1]): # le joueur 1 qui joue
                    score[0]+=1
                else : 
                    score[1]+=1
                break
        else :
            break

    cpt = 0 

    for i in range(coup[0],-1,-1):# on regarde à gauche de la case jouée 
        if( (coup[1]-i > -1 ) and (plateau[coup[0]][coup[1]-i]) == player): 
            cpt+=1
            if (cpt >= 4 ):
                if(jeu[1]):
                    score[0]+=1
                else : 
                    score[1]+=1
                break
            else : 
                break
    cpt = 0 
    for i in range(coup[0],len(plateau)): # on regarde  en dessous de la case jouée 
        if( (coup[0]+i < len(plateau) ) and (plateau[coup[0]+i][coup[1]]) == player): 
            cpt+=1
            if (cpt >= 4 ):
                if(jeu[1]):
                    score[0]+=1
                else : 
                    score[1]+=1
                break
        else :
            break
    
    cpt = 0 

    for i in range(coup[0],len(plateau[coup[0]])): # on regarde  en diagonale (bas-droite) de la case jouée 
        c = coup[0]+i
        if( (c < len(plateau) and (coup[1]+i) < len(plateau[coup[0]])) and (plateau[c][coup[1]+i]) == player): 
            cpt+=1
            if (cpt >= 4 ):
                if(jeu[1]):
                    score[0]+=1
                else : 
                    score[1]+=1
                break
        else : 
            break
    cpt = 0 
    for i in range(coup[0],-1,-1): # on regarde  en diagonale (bas-gauche) de la case jouée 
        c = coup[0]+i
        if( ( c < len(plateau) and (coup[1]-i > -1 )) and (plateau[c][coup[1]-i]) == player): 
            cpt+=1
            if (cpt >= 4 ):
                if(jeu[1]):
                    score[0]+=1
                else : 
                    score[1]+=1
                break
        else : 
            break
    

def saisieCoup(jeu,coup):
    jeu[3].append(coup)
    plateau=jeu[0]
    if (jeu[1]==1):
        plateau[coup[0]][coup[1]]='X'
    else : 
        plateau[coup[0]][coup[1]]='O'

    maj_score(jeu,coup,jeu[4])
    print("SCORE : ",jeu[4])
    jeu[1] = jeu[1]%2+1
    jeu[2] = None


def finalisePartie(jeu):
    """ rien à faire """
