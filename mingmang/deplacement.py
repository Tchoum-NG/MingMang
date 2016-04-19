from main import *
from gui import *
from affiche import *
import affiche
import gui
import math



#0=vide 1=blanc 2=noir
#LES NOIRS COMMENCENT TOUJOURS
#tour=0-> joueur 1 propriétaire        tour=1-> joueur 2 invité (ou ia)
################################ VERIFICATIONS VICTOIRE ###############################
def victoirepions():
    noirs=0
    blancs=0
    for i in affiche.g:
        for j in i:
            if j==1:
                blanc+=1
            if j==2:
                noirs+=1
    if blancs==0:
        print("victoire des noirs")
    elif noirs==0:
        print("victoire des blancs")

def verifdeplacement(coord1,coord2,tour):
    if int(coord1[0])-int(coord2[0])!=0 and int(coord1[1])-int(coord2[1])!=0 :
        print("déplacement invalide : vous ne pouvez bouger qu'en ligne ou colonne")
        return False
    
    if affiche.g[(coord2[0])][(coord2[1])]!=0:
        print("vous ne pouvez pas déplacer votre pion sur un autre pion")
        return False
    
    
    nbmvm=0
    sens=0
    if ((coord1[0])-(coord2[0])) >= 1:
        sens=1
        nbmvm=((coord1[0])-(coord2[0]))
    if ((coord1[1])-(coord2[1])) >= 1:
        sens=2
        nbmvm=((coord1[1])-(coord2[1]))
    if ((coord2[0])-(coord1[0])) >= 1:
        sens=3
        nbmvm=((coord2[0])-(coord1[0]))
    if ((coord2[1])-(coord1[1])) >= 1:
        sens=4
        nbmvm=((coord2[1])-(coord1[1]))

    if nbmvm>=1:
        if sens==4:
            for i in range (1,nbmvm):
                if affiche.g[coord1[0]][coord1[1]+i] !=0:
                    return False
            return True
        if sens==3:
            for i in range (1,nbmvm):
                if affiche.g[coord1[0]+i][coord1[1]] !=0:
                    return False
            return True
        if sens==2:
            for i in range (1,nbmvm):
                if affiche.g[coord1[0]][coord1[1]-i] !=0:
                      return False
            return True
        if sens==1:
            for i in range (1,nbmvm):
                if affiche.g[coord1[0]-i][coord1[1]] !=0:
                      return False
            return True

    else:
        return True


def captured(coord2,tour,taille):
    if tour==1:
        capt=2
    elif tour==2:
        capt=1

    for i in range(1,taille-coord2[1]):#droite
        if affiche.g[coord2[0]][coord2[1]+i]==tour:
            print("capture droite detectée , changement de la couleur des pions")
            for x in range(i):
                affiche.g[coord2[0]][coord2[1]+x]=tour
            captureb(coord2,tour,taille)
            break
        if affiche.g[coord2[0]][coord2[1]+i]==0:
            print("pas de capture detectée")
            captureb(coord2,tour,taille)
            break

def captureb(coord2,tour,taille):
    if tour==1:
        capt=2
    elif tour==2:
        capt=1

    for i in range(1,taille-coord2[0]):#bas
        if affiche.g[coord2[0]+i][coord2[1]]==tour:
            print("capture bas detectée , changement de la couleur des pions")
            for x in range(i):
                affiche.g[coord2[0]+x][coord2[1]]=tour
            captureg(coord2,tour,taille)
            break
        if affiche.g[coord2[0]][coord2[1]+i]==0:
            print("pas de capture detectée")
            captureg(coord2,tour,taille)
            break

def captureg(coord2,tour,taille):
    if tour==1:
        capt=2
    elif tour==2:
        capt=1

    for i in range(1,coord2[0]):
        if affiche.g[coord2[0]][coord2[1]-i]==tour:
            print("capture gauche detectée , changement de la couleur des pions")
            for x in range(i):
                affiche.g[coord2[0]][coord2[1]-x]=tour
            captureh(coord2,tour,taille)
            break
        if affiche.g[coord2[0]][coord2[1]-i]==0:
            print("pas de capture detectée")
            captureh(coord2,tour,taille)
            break
        
def captureh(coord2,tour,taille):   
    if tour==1:
        capt=2
    elif tour==2:
        capt=1

    for i in range(1,taille-coord2[0]):
        if affiche.g[coord2[0]-i][coord2[1]]==tour:
            print("capture haut detectée , changement de la couleur des pions")
            for x in range(i):
                affiche.g[coord2[0]-x][coord2[1]]=tour
            break
        if affiche.g[coord2[0]-i][coord2[1]]==0:
            print("pas de capture detectée")
            break


def calculzone(taille):
    #renvoie un tuple(blanc,noir) ou a correspond
    #a la zone détenue par le joueur 1
    #b a la zone détenue par le joueur 2
    #(droite,gauche,haut,bas)
    a=0
    b=0
    for i in range(taille):
        for j in range(taille):
            if affiche.g[i][j]!=0:
                case=[0,0,0,0]
                for k in range(1,taille-j):#droite
                    if affiche.g[i][j+k]!=0:
                          case[0]=affiche.g[i][j+k]
                for k in range(1,j):#gauche
                    if affiche.g[i][j-k]!=0:
                          case[1]=affiche.g[i][j+k]
                for k in range(1,taille-i):#haut
                    if affiche.g[i+k][j]!=0:
                          case[3]=affiche.g[i][j+k]
                for k in range(1,i):#bas
                    if affiche.g[i-k][j]!=0:
                          case[4]=affiche.g[i][j+k]
            if case.count(1)<=1 and case.count(2)==0:
                if g[i][j]==1:
                    a+=1
            if case.count(2)<=1 and case.count(1)==0:
                if g[i][j]==2:
                    b+=1
    return (a,b)
                
                
            
    

                
############################ JOUEUR CONTRE JOUEUR EN LOCAL ############################



def jcj(tour,taille):
    coord1=[0,0]
    coord2=[0,0]
    mode=1
    print("au tour du joueur ",tour)
    print("Choisissez un pion a déplacer")
    coord1[0]=entreecoord1()
    coord1[1]=entreecoord2()
    print(coord1)
    if int(affiche.g[int(coord1[0])][int(coord1[1])]) != int(tour):
        print("selection invalide , vous devez choisir un de vos pions")
        jcj(tour,taille)
    print("choisissez ou déplacer votre pion")
    coord2[0]=entreecoord1()
    coord2[1]=entreecoord2()
    print(coord2)
    if coord1[0]==coord2[0] and coord1[1]==coord2[1]:
        print("le joueur",tour,"passe son tour")
        toursuivant(mode,tour,taille,passe,1)
    if verifdeplacement(coord1,coord2,tour) :#and veriftour(coord1,coord2):
        (affiche.g[coord1[0]][coord1[1]])=0
        (affiche.g[coord2[0]][coord2[1]])=int (tour)
        captured(coord2,tour,taille)
        zone=calculzone(taille)
    else:
        jcj(tour,taille)
    if zone[0]==(math.ceil(taille/2)):
        print("zone des blancs superieure a la moitié du plateau , gg blancs")
    elif zone[1]==(math.ceil(taille/2)):
        print("zone des blancs superieure a la moitié du plateau , gg blancs")
        
    if  victoirepions()
    else:

        jcj(tour,taille)


        
        







############################ JOUEUR CONTRE IA FACILE############################

def jciafacile(tour,taille):
    print("jeuia facile")




############################ JOUEUR CONTRE IA DIFFICILE############################


def jciadifficile(tour,taille):
    print("jeuiadifficile")


############################ JOUEUR CONTRE JOUEUR EN RESEAU ############################


def jcjr(tour,taille):
    print("jcj en réseau")










