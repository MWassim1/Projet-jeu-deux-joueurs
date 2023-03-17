#!/usr/bin/env python
# -*- coding: utf-8 -*-


            
def initialisePlateau() : 

    plateau = []
    for i in range (0,8) :
        liste = [0,0,0,0,0,0,0,0]
        plateau.append(liste)
    plateau[3][3] = 1
    plateau[4][4] = 1
    plateau[3][4] = 2
    plateau[4][3] = 2
    return plateau

def initialiseScore():
    return [2,2]


def listeCoupsValides(jeu) : 
    listeCoups = [] ; listeCoups2 = [] 
    for i in range (0,len(jeu[0])) :
        for j in range (0,len(jeu[0][i])) : 
            listeCoups += CoupValide(jeu,jeu[1],i,j,0,1)+CoupValide(jeu,jeu[1],i,j,0,-1)+CoupValide(jeu,jeu[1],i,j,-1,0)+CoupValide(jeu,jeu[1],i,j,1,0)+CoupValide(jeu,jeu[1],i,j,-1,1)+CoupValide(jeu,jeu[1],i,j,1,1)+CoupValide(jeu,jeu[1],i,j,-1,-1)+CoupValide(jeu,jeu[1],i,j,1,-1)
# Recupère les coups valides à/en : droite           /       gauche             /             haut          /               bas             /              haut-droite          /              bas-droite         /          haut-gauche               /           bas-gauche
    for i in listeCoups : 
        if i not in listeCoups2 : 
            listeCoups2.append(i)

    return listeCoups2


def CoupValide(jeu,joueur,i,j,x,y):
    listeCoups= []
    plateau=jeu[0]
    if ((i<=7 and i >=0) and (j <= 7 and j >=0) and (joueur ==  plateau[i][j]) ): 
        n = i+x ; m = j+y
        while ((n<=7 and n >=0) and (m <= 7 and  m>=0) and (plateau[n][m] == joueur%2+1) ) :
            m+=y; n+=x
            if ((n<=7 and n >=0) and (m <= 7 and m >=0) and plateau[n][m] == 0) :
                listeCoups.append([n,m])
                break
    return listeCoups



def comptePion(jeu,coup,n,m,combo):
    """
        n : int -> incrémente ou non "l" (ligne) 
        m : int -> incrémente ou non "c" (colonne)
        combo : list[bool] 
                                                                """

    plateau=copie_plateau(jeu)
    l=coup[0]+n; c = coup[1]+m 
    score=copie_score(jeu)
    trouve_pion_adverse = False
    if ( not combo[0] ): 
        if (jeu[1] == 1) : 
            score[0]+=1
        else : 
            score[1]+=1
   # while((plateau[l][c] != jeu[1]) and (plateau[l][c] != 0) and ((c != maxc) and (l != maxl ))):
    if ((c<=7 and c >=0) and (l <= 7 and l >=0)):
        while((c<=7 and c >=0) and (l <= 7 and l >=0) and  (plateau[l][c] != jeu[1]) and (plateau[l][c] != 0)):
            trouve_pion_adverse = True 
            plateau[l][c] = jeu[1]
            if(jeu[1] == 1 ):
                score[0]+=1
                score[1]-=1
            else :
                score[0]-=1
                score[1]+=1
            c+=m ; l+=n
        if (((c<=7 and c >=0) and (l <= 7 and l >=0)) and (plateau[l][c] == jeu[1]) and ( trouve_pion_adverse)) :
            jeu[0]=plateau
            jeu[4] = score
            combo[0] = True
    return jeu[4]


def finalisePartie(jeu):
    """
        corps de fonction vide car , il n'y a rien  a faire 
                                                        """
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

def copie_score(jeu) : 
    score=jeu[4]
    copie_score=[]
    for i in score:
        copie_score.append(i)
    return copie_score

def saisieCoup(jeu,coup): 
    plateau=jeu[0]
    joueur=jeu[1]
   # plateau=copie_plateau(jeu)
    if (joueur == 1): 
        plateau[coup[0]][coup[1]] = 1 
    else :
        plateau[coup[0]][coup[1]] = 2
    # On vérifie s'il y a des pions adverses autour du pion joué  et met le score à jour si nécessaire 
    combo= [False] 
    jeu[4] = comptePion(jeu,coup,0,1,combo) # a droite
    jeu[4] = comptePion(jeu,coup,0,-1,combo) # à gauche
    jeu[4] = comptePion(jeu,coup,-1,0,combo) # en haut 
    jeu[4] = comptePion(jeu,coup,1,0,combo) # en bas
    jeu[4] = comptePion(jeu,coup,1,1,combo) # en bas à droite 
    jeu[4] = comptePion(jeu,coup,-1,1,combo) # en haut à droite 
    jeu[4] = comptePion(jeu,coup,1,-1,combo) # en bas à gauche 
    jeu[4] = comptePion(jeu,coup,-1,-1,combo)# en haut à gauche 
    jeu[2] = None
    jeu[1] = jeu[1]%2+1
    jeu[3].append(coup)
