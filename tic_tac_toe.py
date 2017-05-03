import random
import sys
from itertools import combinations
import itertools
import numpy
from numpy import *

temp_list=[]

# Main Class where the game is played with two players (Player class)
class Game: 

    #initialize
    def __init__(self,player1,player2,winning_combo):

        self.player1=player1
        self.player2=player2
        self.winning_combo=winning_combo

    #set the winning combo for n*n matrix
    def set_board(self,n):
         self.winning_combo=[]
         temp_matrix=[[[] for i in range(n)] for i in range(n)]
         count=1
         for i in range(n):
             for j in range(n): 
                temp_matrix[i][j]=count
                count=count+1
         #print temp_matrix
         for row in temp_matrix:
             self.winning_combo.append(row)
         #print self.winning_combo
         transpose_matrix = numpy.transpose(temp_matrix)
         #print transpose_matrix
         for row in transpose_matrix:
             self.winning_combo.append(list(row))
         diagonal_value=numpy.diagonal(temp_matrix)
         self.winning_combo.append(list(diagonal_value))
         opposite_diagonal_value=numpy.diag(numpy.fliplr(temp_matrix))
         self.winning_combo.append(list(opposite_diagonal_value))
         #print self.winning_combo
   
    def play(self,player,value):
        player.value_list.append(value)

   #check if the player met the winning condition
    def check(self,input_check_list,winning_combo,n):
       
        combinations=itertools.combinations(input_check_list,n)
        combinations_list = [list(x) for x in combinations]
        for i in combinations_list:
            #print i
            for j in winning_combo:
                if sorted(i)==sorted(j):
            #if i in winning_combo:
                    return True
        return False  
        
        
        
#Player class inherited from Game class
class Player(Game):

    def __init__(self,name,value_list):

        self.name=name
        self.value_list=value_list

#check the input from the player whether it is in the range
def check_input(total_length):
    while True:
     value = input("Pick a number in the range of 1 to"+str(total_length)+":")
     if int(value) in range(1,total_length+1)and value not in temp_list:
         temp_list.append(value)
         return value
         break
     else:
         print "Please Enter a value within the range and dont enter the number already used !!!"

#how to board looks sample
def drawboard():
    print ('    |   |   ')
    print ('  1   2    3 ' )
    print ('    |   |    ')
    print ('---------------')
    print ('    |   |   ')
    print ('  4   5     6' )
    print ('    |   |   ')
    print('-----------------')
    print ('    |   |   ')
    print ('  7   8     9' )
    print ('    |   |   ')
    print 

#instructions
def howtoplay():
    print
    print "** Given Example of 3*3 matrix board(it can be any n*n)"
    print "** Each player should enter a integer value based on the position"
    print "** Remaining Rules are same as TIC TAC TOE except 'O'and 'X' you need to enter the position you need"
    print
    
print "TWO PLAYER GAME"
print
drawboard()
howtoplay()

p1_name=raw_input("Player 1 - Enter your Name:")
print p1_name
p2_name=raw_input("Player 2 - Enter your Name:")
print p2_name
player1=Player(p1_name,[])
player2=Player(p2_name,[])
game= Game(player1,player2,[])
count_1=0
count_2=0
flag=0

print "Enter the size of the board(3- 3*3,4- 4*4):"
n=input()

game.set_board(n)


##print "CHOOSING TOSS ENTER 1 or 2--p1 enter:"
##toss_input=input()
##print toss_input
##toss_result=random.randint(1,2)
##print toss_result
##if toss_input==toss_result:
##    print "P1 will play first-won toss"
##else:
##    print "P2 will play second-won toss"

#print game.winning_combo

total_length=n*n
for i in range(1,total_length+1):
    
    if i%2 !=0 :
        print player1.name+'\'s turn'
        input_position=check_input(total_length)
        #input_position=input("Pick a number in the range of 1 to"+str(total_length)+":")
        count_1=count_1+1
        game.play(player1,input_position)
        if count_1>=n:
            check_value=game.check(player1.value_list,game.winning_combo,n)
            if check_value is True:
                print
                print player1.name+" wins"
                flag = 1
                break

    elif i%2 ==0:

        print player2.name+'\'s turn'
        input_position=check_input(total_length)
        #input_position=input("Pick a number in the range of 1 to"+str(total_length)+":")
        count_2=count_2+1
        game.play(player2,input_position)
        if count_2>=n:
            check_value=game.check(player2.value_list,game.winning_combo,n)
            if check_value is True:
                print
                print player2.name+" wins"
                flag = 1
                break

if flag ==0:
    print
    print player1.name+" and "+player2.name+" Played Well !!!"
    print 'MATCH DRAWN'

        



        
