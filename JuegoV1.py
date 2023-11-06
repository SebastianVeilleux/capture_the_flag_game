import numpy as np
from colorama import Fore

ROWS = 7
COLUMNS = 5
#Creates the board
board = np.full((ROWS, COLUMNS),None)

#Default winner to none
winner = None

#Defaults turn to Blue Team
turn = 'Red team'

# Teams
RED_TEAM = ['R1','Rf','R2']
BLUE_TEAM = ['B1','Bf','B2']

#Set start positions
board[0,1:4] = RED_TEAM
board[ROWS-1,1:4] = BLUE_TEAM


def get_frame():
    global board
    board = np.flip(board,0)
    print('\n\n\n\n')
    print('\t \t    UP\n')
    print(f'\t{board[0]}')
    print(f'\t{board[1]}')
    print(f'\t{board[2]}')
    print(f'\t{board[3]}')
    print(f'LEFT    {board[3]}    RIGHT')
    print(f'\t{board[4]}')
    print(f'\t{board[5]}')
    print(f'\t{board[6]}')
    print('\n')
    print('\t \t   DOWN\n')
    print(' ')
    
get_frame()

def get_coord(name):
    global board
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == name:
                return [i,j]
    

def get_name(Coord):
    global board
    nombre = board[Coord[0]][board[0][1]]
    return[nombre]


def move_up(Player):
    global board
    coord = get_coord(Player)
    new_coord = board[coord[0]-1][coord[1]]

    if coord[0]>=0 and new_coord == None:#Validates if the new position is empty
        board[coord[0]-1][coord[1]] = board[coord[0]][coord[1]]
        board[coord[0]][coord[1]] = None
    elif coord[0]>=0 and new_coord != None:#Validates if the new position is not empty
        pass

    get_frame()

def move_down(Player):
    global board
    coord = get_coord(Player)
    new_coord = board[coord[0]+1][coord[1]]

    if coord[0]>=0 and new_coord == None:#Validates if the new position is empty
        board[coord[0]+1][coord[1]] = board[coord[0]][coord[1]]
        board[coord[0]][coord[1]] = None
    elif coord[0]>=0 and new_coord != None:#Validates if the new position is not empty
        pass
        
    get_frame()

def move_left(Player):
    global board
    coord = get_coord(Player)
    new_coord = board[coord[0]][coord[1]-1]

    if  new_coord == None:#Validates if the new position is empty
        board[coord[0]][coord[1]-1] = board[coord[0]][coord[1]]
        board[coord[0]][coord[1]] = None
    elif coord[0]>=0 and new_coord != None:#Validates if the new position is not empty
        pass
    
    get_frame()

def move_right(Player): #Falta arregla la teletransportacion
    global board
    coord = get_coord(Player)
    
    if coord[1] >= len(board[0]) - 1: 
        dest_col =0
    else:
        dest_col = coord[1] + 1

    if board[coord[0]][dest_col] == None:
        print('Si entre')
        board[coord[0]][dest_col] = board[coord[0]][coord[1]]
        board[coord[0]][coord[1]] = None
    
    get_frame()
        


while winner == None:
    print(len(board))
    # Input jugador y movimiento
    if turn == 'Blue team':
        print(Fore.BLUE + '\n' + turn + ' turn')
        player = 'B' + input('Player: B')
        move = input('Move (up, right, left, down): ') 
    else:
        print(Fore.RED + '\n' + turn + ' turn')
        player = 'R' + input('Player: R')
        move = input('Move (up, right, left, down): ')

    # Moves the player  based on the input
    if move=='up':
        move_up(player)
    elif move=='down':
        move_down(player)
    elif move == ('left'):
        move_left(player)
    elif move == ('right'):
        move_right(player)
    
    # Check for winner
    if board[6][2]=='B1Rf' or board[6][2]=='B2Rf':
        winner = 'Blue team'
    elif board[0][2]=='R1Rf' or board[0][2]=='R2Rf':
        winner = 'Red Team'

    # Change turn
    if turn == 'Blue team':
        turn = 'Red team'
    else:
        turn = 'Blue team'



print('\nThe Winner is the ' + winner + '!')