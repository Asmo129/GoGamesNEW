
#The verification of suicide and the count of the point (not for the kill point) is missing but the game is completed
#LIST, VARIABLE AND IMPORT
from listego import *
import time
import random
list_stone_to_kill=[]#list for verification
list_stone_to_survive_E=[]
list_stone_to_survive_O=[]
list_stone_to_survive_S=[]
list_stone_to_survive_N=[]
killBlack=0#Kill
killWhite=0
clockblack=500#Clock
clockwhite=500
BcooXY=(0,0)#KO
WcooXY=(0,0)
compteurpass=0#Pass
######################################################
#FUNCTION
def returncolor (color):#function to transform the lettre in the stone for the goban
    if color=='b':
        return '⚈'#Your computer will maybe make an caracter error due of this, so you can change
    elif color=='w':
        return 'o'
    else:
        return '+'
    
def return_tup(tuple):#function to transform the tuple in two coordone to make addition 
    x1=tuple[0]
    x2=tuple[1]
    return x1,x2

def stone_input (color):#function to take the coordone and the color
    cooXY=input('Coordonnées:')
    cooXY=tuple(int(x) for x in cooXY.split(","))
    add_stone_list (color,cooXY)
    return cooXY

def add_stone (color):#function to print one stone
    color=returncolor (color)
    print( f"-{color}-",end='')

def goban_with_stone ():#function to print the entire goban with the stone
    compteur=0
    compteurcooY=0
    print (' 1  2  3  4  5  6  7  8  9  ')#the X coordone
    for stones in list_stone.values():
        compteur+=1
        add_stone(stones)#the stone
        if compteur==9:
            compteurcooY+=1
            print(f'{compteurcooY}', end='')#the Y coo
            print('\n',end='')
            print(' | '*9)#the line
            compteur=0
    print('')

def add_stone_list (color, coo_to_add):#function to not put a stone on a another stone
    for coordone in list_stone.keys():
        if coordone==coo_to_add:
            color_to_ana=list_stone.get(coordone)
            if color_to_ana!='a':
                print("there is a stone already")
                return 1
            else:
                list_stone[coo_to_add]=color

def clear_list_stone(list,liststone):#function to clear the dead stone
    for cooXY in list:
        liststone[cooXY]='a'

def verif_stone_side_board (cooXY):#function to verife if the stone is on the board
    if cooXY[0]==0 or cooXY[1]==0 or cooXY[0]==10 or cooXY[1]==10:
        return True
    else:
        return False

def NESO_stone (cooXY):#function to change the original coordone
    cooXTomodifie,cooYTomodifie=return_tup(cooXY)
    stoneN=cooXTomodifie,cooYTomodifie-1
    stoneE=cooXTomodifie+1,cooYTomodifie
    stoneS=cooXTomodifie,cooYTomodifie+1
    stoneO=cooXTomodifie-1,cooYTomodifie
    return stoneN,stoneO,stoneE,stoneS

def counterkill(list):#function to count the kill in the game
    if len(list)<=0:
        pass
    else:
        numberkill=len(list)
        return numberkill

def verif_stone_diff(color,cooXY,list):#function to verif one stone 
    if list_stone[cooXY]=='a':#if is empty
        return 1
    elif list_stone[cooXY]!=color:#if is a different stone
        if cooXY not in list:  
            list.append(cooXY)
        return 0
    return 0   
     
def find_to_survive (color,cooXY,list_stone_to_survive_general):#function to verifie the stone around
    compteurA=0
    stoneN,stoneO,stoneE,stoneS=NESO_stone (cooXY)
#EAST
    if verif_stone_side_board (stoneE)==True:
        pass
    else:
        compteurA+=verif_stone_diff(color, stoneE,list_stone_to_survive_general)
#WEST
    if verif_stone_side_board (stoneO)==True:
        pass
    else:
        compteurA+=verif_stone_diff(color, stoneO,list_stone_to_survive_general)
#SOUTH
    if verif_stone_side_board (stoneS)==True:
        pass
    else:
        compteurA+=verif_stone_diff(color, stoneS,list_stone_to_survive_general)
#NORTH
    if verif_stone_side_board (stoneN)==True:
        pass
    else:
        compteurA+=verif_stone_diff(color, stoneN,list_stone_to_survive_general)
    return compteurA


def find_other_side (color,cooXY,list):#function to see all the stone around in one side of the original stone
    compteurAFOS=0
    compteur=0
    while compteur<=50:
        compteurAFOS+=find_to_survive (color,cooXY,list)
        index=random.randrange(0,len(list))
        cooXY=list[index]
        compteur+=1
        if compteurAFOS > 1:
            return compteurAFOS
    return compteurAFOS


def find_other (color,cooXY):#function to see all the stone around of the original stone
#EAST
    global killBlack
    global killWhite
    compteurAFO=0
    if len(list_stone_to_survive_E)==0:
        pass        
    else:
        cooXY=list_stone_to_survive_E[0]
        compteurAFO+=find_other_side (color,cooXY,list_stone_to_survive_E)
        if compteurAFO==0:
            if color=='b':
                killBlack+=counterkill(list_stone_to_survive_E)
            else:
                killWhite+=counterkill(list_stone_to_survive_E)
            clear_list_stone(list_stone_to_survive_E,list_stone)
        del list_stone_to_survive_E [0:len(list_stone_to_survive_E)]
#WEST
    compteurAFO=0
    if len(list_stone_to_survive_O)==0:
        pass        
    else:
        cooXY=list_stone_to_survive_O[0]
        compteurAFO+=find_other_side (color,cooXY,list_stone_to_survive_O)
        if compteurAFO==0:
            if color=='b':
                killBlack+=counterkill(list_stone_to_survive_O)
            else:
                killWhite+=counterkill(list_stone_to_survive_O)
            clear_list_stone(list_stone_to_survive_O,list_stone)
        del list_stone_to_survive_O [0:len(list_stone_to_survive_O)]
#SOUTH
    compteurAFO=0
    if len(list_stone_to_survive_S)==0:
        pass        
    else:
        cooXY=list_stone_to_survive_S[0]
        compteurAFO+=find_other_side (color,cooXY,list_stone_to_survive_S)
        if compteurAFO==0:
            if color=='b':
                killBlack+=counterkill(list_stone_to_survive_S)
            else:
                killWhite+=counterkill(list_stone_to_survive_S)
            clear_list_stone(list_stone_to_survive_S,list_stone)
        del list_stone_to_survive_S [0:len(list_stone_to_survive_S)]
#NORTH
    compteurAFO=0
    if len(list_stone_to_survive_N)==0:
        pass        
    else:
        cooXY=list_stone_to_survive_N[0]
        compteurAFO+=find_other_side (color,cooXY,list_stone_to_survive_N)
        if compteurAFO==0:
            if color=='b':
                killBlack+=counterkill(list_stone_to_survive_N)
            else:
                killWhite+=counterkill(list_stone_to_survive_N)
            clear_list_stone(list_stone_to_survive_N,list_stone)
        del list_stone_to_survive_N [0:len(list_stone_to_survive_N)]


def find_to_kill (color,cooXY):#function to see if it's necessairy to verify the side of the stone putted 
    stoneN,stoneO,stoneE,stoneS=NESO_stone (cooXY)
    if verif_stone_side_board (stoneE)==True:
        pass
    else:
        verif_stone_diff(color, stoneE,list_stone_to_survive_E)

    if verif_stone_side_board (stoneO)==True:
        pass
    else:
        verif_stone_diff(color, stoneO,list_stone_to_survive_O)

    if verif_stone_side_board (stoneS)==True:
        pass
    else:
        verif_stone_diff(color, stoneS,list_stone_to_survive_S)

    if verif_stone_side_board (stoneN)==True:
        pass
    else:
        verif_stone_diff(color, stoneN,list_stone_to_survive_N)           


def save_stone_list ():#function to save the coordone of your game
    fichier = open("liststone.txt", "w")
    fichier.write(str(list_stone)+'\nBlack Kills: '+str(killBlack)+'\nWhite Kills: '+str(killWhite))
    fichier.close()

######################################################
#THE GAME
while True:#The game
    goban_with_stone()#Black Turn

    print ("It's Black turn\n",'\nYou have',clockblack,'secondes\nAnd',killBlack,'kill')#The turn and statistic
    startblack=time.perf_counter()

    oldBcooXY=BcooXY
    BcooXY=input('Coordonnées:')
    if BcooXY=='pass':#if the player pass
        compteurpass+=1
        pass
    else:
        BcooXY=tuple(int(x) for x in BcooXY.split(","))#The input
        while BcooXY==oldBcooXY:
            print("It's a Ko!, choose an another stone to play")#verifi if it's a ko     
            BcooXY=input('Coordonnées:')
            BcooXY=tuple(int(x) for x in BcooXY.split(","))
        add_stone_list('b',BcooXY)#To add the stone in the list

        endblack =time.perf_counter()#the clock
        clockblack-=round(endblack-startblack,0)
        if clockblack<=0:#if the clock is out
            print("You are out in time, You lost")
            break

        find_to_kill('b',BcooXY)#To verify the other stone around and see if we kill
        find_other('b',BcooXY)

    if compteurpass>=2:#To finish the game
        print('The game is over, there is your game and your point')
        save_stone_list()
        break

    goban_with_stone()#White Turn it's the same than the black turn but for white
    print ("It's White turn\n",'\nYou have',clockwhite,'secondes\nAnd',killWhite,'kill')
    startwhite=time.perf_counter()

    oldWcooXY=WcooXY
    WcooXY=input('Coordonnées:')
    if WcooXY=='pass':
        compteurpass+=1
        pass
    else:
        WcooXY=tuple(int(x) for x in WcooXY.split(","))
        while WcooXY==oldWcooXY:
            print("It's a Ko!, choose an another stone to play")
            WcooXY=input('Coordonnées:')
            WcooXY=tuple(int(x) for x in WcooXY.split(","))
        add_stone_list('w',WcooXY)

        endwhite =time.perf_counter()
        clockwhite-=round(endwhite-startwhite,0)#the clock

        if clockwhite<=0:
            print("You are out in time, You lost")
            break

        find_to_kill('w',WcooXY)
        find_other('w',WcooXY)

    if compteurpass>=2:
        print('The game is over, there is your game and your point:')
        save_stone_list()
        break