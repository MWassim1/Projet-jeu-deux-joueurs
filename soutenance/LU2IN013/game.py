#!/usr/bin/env python
# -*- coding: utf-8 -*-

# plateau: List[List[nat]]
# liste de listes (lignes du plateau) d'entiers correspondant aux contenus des cases du plateau de jeu

# coup:[nat nat]
# Numero de ligne et numero de colonne de la case correspondante a un coup d'un joueur

# Jeu
# jeu:[plateau nat List[coup] List[coup] List[nat nat]]
# Structure de jeu comportant :
#           - le plateau de jeu
#           - Le joueur a qui c'est le tour de jouer (1 ou 2)
#           - La liste des coups possibles pour le joueur a qui c'est le tour de jouer
#           - La liste des coups joues jusqu'a present dans le jeu
#           - Une paire de scores correspondant au score du joueur 1 et du score du joueur 2

game=None #Contient le module du jeu specifique: awele ou othello
joueur1=None #Contient le module du joueur 1
joueur2=None #Contient le module du joueur 2


#Fonctions minimales 

def getCopieJeu(jeu):
    """ jeu->jeu
        Retourne une copie du jeu passe en parametre
        Quand on copie un jeu on en calcule forcement les coups valides avant
    """
    jeu2=[]

    plateau = jeu[0]
    copie_plateau = []
    liste = []
    for i in range (0,len(plateau)):
        for j in range (0,len(plateau[i])):
            liste.append(plateau[i][j])
        copie_plateau.append(liste)
        liste=[]
    
    liste_coup=jeu[3]
    copie_liste_coup=[]
    for i in liste_coup:
        copie_liste_coup.append(i)

    score=jeu[4]
    copie_score=[]
    for i in score:
        copie_score.append(i)

    joueur=jeu[1]
    coup_valide=getCoupsValides(jeu)
    jeu2.append(copie_plateau)
    jeu2.append(joueur)
    jeu2.append(coup_valide)
    jeu2.append(copie_liste_coup)
    jeu2.append(copie_score)
    return jeu2



def finJeu(jeu):
    """ jeu -> bool
        Retourne vrai si c'est la fin du jeu
    """
    return (getCoupsValides(jeu)==[])



def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
        On suppose que la fonction n'est appelee que si il y a au moins un coup valide possible
        et qu'elle retourne obligatoirement un coup valide
    """
    joueur = joueur1
    if  jeu[1] == 2 : 
        joueur = joueur2
    coup = joueur.saisieCoup(getCopieJeu(jeu))
    return game.saisieCoup(jeu,coup)

def getCoupsValides(jeu):
    """ jeu  -> List[coup]
        Retourne la liste des coups valides dans le jeu passe en parametre
        Si None, alors on met � jour la liste des coups valides
    """

    if jeu[2] is None: 
        jeu[2]=game.listeCoupsValides(jeu)
    return jeu[2]

def coupValide(jeu,coup):
    """jeu*coup->bool
        Retourne vrai si le coup appartient a la liste de coups valides du jeu
   """
    Listcoups = getCoupsValides(jeu)
    #print("\nListe de coups possible : ",Listcoups,"\nCoup joué : ",coup,"\n")
    if coup in Listcoups :
       return True
    return False



def joueCoup(jeu,coup):
    """jeu*coup->void
        Joue un coup a l'aide de la fonction joueCoup defini dans le module game
        Hypothese:le coup est valide
        Met tous les champs de jeu à jour (sauf coups valides qui est fixée à None)
    """
    if (coupValide(jeu,coup)):
        game.saisieCoup(jeu,coup)


def initialiseJeu():
    """ void -> jeu
        Initialise le jeu (nouveau plateau, liste des coups joues vide, liste des coups valides None, scores a 0 et joueur = 1)
    """
    jeu = [game.initialisePlateau(),1,None,[],game.initialiseScore()]
    return jeu

def getGagnant(jeu):
    """jeu->nat
    Retourne le numero du joueur gagnant apres avoir finalise la partie. Retourne 0 si match nul
    """
    game.finalisePartie(jeu)
    g = 0 
    if jeu[4][0] > jeu[4][1] : 
        g = 1 
    if jeu[4][0] < jeu[4][1]: 
        g = 2 

    return g 
    

def affiche(jeu):
    """ jeu->void
        Affiche l'etat du jeu de la maniere suivante :
                 Coup joue = <dernier coup>
                 Scores = <score 1>, <score 2>
                 Plateau :

                         |       0     |     1       |      2     |      ...
                    ------------------------------------------------
                      0  | <Case 0,0>  | <Case 0,1>  | <Case 0,2> |      ...
                    ------------------------------------------------
                      1  | <Case 1,0>  | <Case 1,1>  | <Case 1,2> |      ...
                    ------------------------------------------------
                    ...       ...          ...            ...
                 Joueur <joueur>, a vous de jouer
                    
         Hypothese : le contenu de chaque case ne depasse pas 5 caracteres
    """
    if(jeu[3] == []):
        print("\nCoup joue = < Aucun coup joue >\n")
    else :
        print("Coup joue = ",jeu[3][len(jeu[3])-1],"\n")
    print("Scores = ",getScore(jeu,1)," , ",getScore(jeu,2),"\n")
    print("Plateau : \n\n")
    plateau = jeu[0]
    print("\t|",end='')
    for i in range (0,len(plateau[0])) : 
        print("\t",i," \t|",end='')

   
    print("\n----------",end='')  
    for j in range (0,len(plateau[0])) :
        print("----------------",end='')      
    print("\n")
    for i in range (0,len(plateau)) :
        print(" ",i," ",end='')
        for j in range (0,len(plateau[i])) :
            print(" \t|\t",plateau[i][j],end='')
        print(" \t|\n----------",end='') 
        for j in range (0,len(plateau[0])) :
            print("----------------",end='')   
            
        print("\n")
    print("Joueur ",jeu[1]," a vous de jouer \n")

# Fonctions utiles

def getPlateau(jeu):
    """ jeu  -> plateau
        Retourne le plateau du jeu passe en parametre
    """
    
    return jeu[0]

def getCoupsJoues(jeu):
    """ jeu  -> List[coup]
        Retourne la liste des coups joues dans le jeu passe en parametre
    """
    return jeu[3]



def getScores(jeu):
    """ jeu  -> Pair[nat nat]
        Retourne les scores du jeu passe en parametre
    """
    return jeu[4]

def getJoueur(jeu):
    """ jeu  -> nat
        Retourne le joueur a qui c'est le tour de jouer dans le jeu passe en parametre
    """
    joueur=jeu[1]
    return joueur


def changeJoueur(jeu):
    """ jeu  -> void
        Change le joueur a qui c'est le tour de jouer dans le jeu passe en parametre (1 ou 2)
    """
    if (jeu[1]) :
        jeu[1] =  2 
    else :
        jeu[1] = 1 

def getScore(jeu,joueur):
    """ jeu*nat->int
        Retourne le score du joueur
        Hypothese: le joueur est 1 ou 2
    """
    if (joueur==1):
        return jeu[4][0] # Retourne le score du joueur 1 
    return jeu[4][1] # Retourne le score du joueur 2 

def getCaseVal(jeu, ligne, colonne):
    """ jeu*nat*nat -> nat
        Retourne le contenu de la case ligne,colonne du jeu
        Hypothese: les numeros de ligne et colonne appartiennent bien au plateau  : ligne<=getNbLignes(jeu) and colonne<=getNbColonnes(jeu)
    """
    return jeu[0][ligne][colonne]
    
    




