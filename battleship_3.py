from random import randint
import os
clear = lambda: os.system('cls')

class Ship(object):
    def __init__(self, size):
        self.size = size
        self.posns = []
        up_or_down = randint(1,2)
        if up_or_down == 1:
            self.x = randint(1,11-size)
            self.y = randint(1,size)
            self.posns.append([self.x,self.y])
            for i in range(1, size):
                self.posns.append([self.x+i,self.y])
        elif up_or_down == 2:
            self.x = randint(1,size)
            self.y = randint(1,11-size)
            self.posns.append([self.x,self.y])
            for i in range(1, size):
                self.posns.append([self.x,self.y+i])

class userShip(object):
    def __init__(self, size):
        self.size = size
        self.posns = []
        max_coord = 11 - self.size
        up_or_down = randint(1,2)
        if up_or_down == 1:
            try:
                self.x = input('Enter a number between 1 and '+str(max_coord)+': ')
                if self.x not in range(1, max_coord+1):
                    print
                    print 'Really? You\'re trying to cheat already?'
                    print 'Now you don\'t get to pick the number; I\'ll pick it for you.'
                    print
                    self.x = randint(1, max_coord)
            except:
                print
                print 'Seriously?'
                print
                self.x = randint(1, max_coord)
            try:
                self.y = input('Enter a number between 1 and 10: ')
                if self.y not in range(1, 11):
                    print
                    print 'Really? You\'re trying to cheat already?'
                    print 'Now you don\'t get to pick the number; I\'ll pick it for you.'
                    print
                    self.y = randint(1, 10)
            except:
                print
                print 'Seriously?'
                print
                self.y = randint(1, 10)
            self.posns.append([self.x,self.y])
            for i in range(1, size):
                self.posns.append([self.x+i,self.y])
        elif up_or_down == 2:
            try:
                self.x = input('Enter a number between 1 and 10: ')
                if self.x not in range(1, 11):
                    print
                    print 'Really? You\'re trying to cheat already?'
                    print 'Now you don\'t get to pick the number; I\'ll pick it for you.'
                    print
                    self.x = randint(1, 10)
            except:
                print
                print 'Seriously?'
                print
                self.x = randint(1, 10)
            try:
                self.y = input('Enter a number between 1 and '+str(max_coord)+': ')
                if self.y not in range(1, max_coord+1):
                    print
                    print 'Really? You\'re trying to cheat already?'
                    print 'Now you don\'t get to pick the number; I\'ll pick it for you.'
                    print
                    self.y = randint(1, max_coord)
            except:
                print
                print 'Seriously?'
                print
                self.y = randint(1, max_coord)
            self.posns.append([self.x,self.y])
            for i in range(1, size):
                self.posns.append([self.x,self.y+i])
        
def checkForOverlap(shipA, shipB):
    for posn in shipA.posns:
        if posn in shipB.posns:
            return True
    else:
        return False

cship_1 = Ship(randint(3,5))
cship_2 = Ship(randint(3,5))
while checkForOverlap(cship_2, cship_1):
    cship_2 = Ship(randint(3,5))
cship_3 = Ship(randint(3,5))
while checkForOverlap(cship_3, cship_1) or checkForOverlap(cship_3, cship_2):
    cship_3 = Ship(randint(3,5))
##print cship_1.posns, cship_2.posns, cship_3.posns

print '========================================================='
print 'Set up your own ships.'
print '========================================================='
pship_1 = userShip(randint(3,5))
pship_2 = userShip(randint(3,5))
while checkForOverlap(pship_2, pship_1):
    pship_2 = userShip(randint(3,5))
pship_3 = userShip(randint(3,5))
while checkForOverlap(pship_3, pship_1) or checkForOverlap(pship_3, pship_2):
    pship_3 = userShip(randint(3,5))
##print pship_1.posns, pship_2.posns, pship_3.posns
clear()

def new_board():
    board = []
    for i in range(10):
        board.append(['O']*10)
    return board

def print_board(board):
    col_nums = []
    for i in range(1,11):
        col_nums.append(str(i))
    print '   ', '   '.join(col_nums)
    print #'  '+'---+'*10
    row_num = 1
    for row in board:
        if row_num != 10:
            print ' '+ str(row_num) + '  ' + '   '.join(row)
            print #'  '+'---+'*10
            row_num += 1
        else:
            print str(row_num) + '  ' + '   '.join(row)


attack_board = new_board()
#print_board(attack_board)
defense_board = new_board()
##for posn in pship_1.posns:
##    defense_board[posn[0]-1,][posn[1]-1] = 'X'
##for posn in pship_2.posns:
##    defense_board[posn[0]-1,][posn[1]-1] = 'X'
##for posn in pship_3.posns:
##    defense_board[posn[0]-1,][posn[1]-1] = 'X'

print '========================================================='
print 'Rows: 1-10, Columns: 1-10. You go first.'
print '========================================================='
print 'Vamonos muchacho. Vas a perder, puto. Hehehe.'
print '========================================================='
print_board(attack_board)
print


while (len(cship_1.posns) > 0 or len(cship_2.posns) > 0 or len(cship_3.posns) > 0) \
      and (len(pship_1.posns) > 0 or len(pship_2.posns) > 0 or len(pship_3.posns) > 0):
    try:
        guess_row = int(input('Guess a row: '))
        guess_col = int(input('Guess a column: '))
        if guess_row not in range(1,11) or guess_col not in range(1,11):
            print 'C\'mon man, make a real guess.'
            continue
    except:
        print 'C\'mon man, make a real guess.'
        continue
    clear()
    print '========================================================='
    if attack_board[guess_row-1][guess_col-1] == '-':
        print 'You already guessed that one.'
    elif [guess_row, guess_col] in cship_1.posns:
        print 'Hit...'
        cship_1.posns.remove([guess_row, guess_col])
        if len(cship_1.posns) == 0:
            print '...AND SUNK!'
        attack_board[guess_row-1][guess_col-1] = 'X'
    elif [guess_row, guess_col] in cship_2.posns:
        print 'Hit...'
        cship_2.posns.remove([guess_row, guess_col])
        if len(cship_2.posns) == 0:
            print '...AND SUNK!'
        attack_board[guess_row-1][guess_col-1] = 'X'
    elif [guess_row, guess_col] in cship_3.posns:
        print 'Hit...'
        cship_3.posns.remove([guess_row, guess_col])
        if len(cship_3.posns) == 0:
            print '...AND SUNK!'
        attack_board[guess_row-1][guess_col-1] = 'X'
    else:
        print 'Missssss'
        attack_board[guess_row-1][guess_col-1] = '-'
    print '========================================================='
    print 'LENGTH OF YOUR SHIPS:', len(pship_1.posns), ';', len(pship_2.posns), ';', len(pship_3.posns)
    print '========================================================='
    print_board(attack_board)
    print
    count = 0
    while count < 8:
        cguess_row = randint(1,10)
        cguess_col = randint(1,10)
        if [cguess_row, cguess_col] in pship_1.posns:
            pship_1.posns.remove([cguess_row,cguess_col])
        elif [cguess_row, cguess_col] in pship_2.posns:
            pship_2.posns.remove([cguess_row,cguess_col])
        elif [cguess_row, cguess_col] in pship_3.posns:
            pship_3.posns.remove([cguess_row,cguess_col])
        count += 1

if len(cship_1.posns) == 0 and len(cship_2.posns) == 0 and len(cship_3.posns) == 0:
    print 'YOU WON THE GAME'
    print
    print '...you got lucky this time'
    print
elif len(pship_1.posns) == 0 and len(pship_2.posns) == 0 and len(pship_3.posns) == 0:
    print 'HA YOU JUST LOST TO A COMPUTER THAT GUESSED AT RANDOM!'
    print 
    print 'My board was:'
    print
    for posn in cship_1.posns:
        attack_board[posn[0]-1][posn[1]-1] = 'X'
    for posn in cship_2.posns:
        attack_board[posn[0]-1][posn[1]-1] = 'X'
    for posn in cship_3.posns:
        attack_board[posn[0]-1][posn[1]-1] = 'X'
    print_board(attack_board)
    print
end_game = 0
while end_game == 0:
    end_game = input('To end game, press Enter ')
