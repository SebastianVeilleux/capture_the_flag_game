import numpy as np

#Create board
ROWS = 7
COLUMNS = 5
board = np.full((ROWS, COLUMNS),None)


winner = None
turn = 'Red team'

# Teams & Characters
RED_TEAM = ['R1','Rf','R2']
BLUE_TEAM = ['B1','Bf','B2']

characters = {
    "R1":'👹',
    "R2":'👺',
    "B1":'😇',
    "B2":'👼'
}

#Set start positions
board[0,1:4] = characters['R1'], RED_TEAM[1], characters['R2']
board[ROWS-1,1:4] = characters['B1'], RED_TEAM[1], characters['B2']

#Prints the board
def get_frame():
    global board
    board = np.flip(board,0)
    print('\n\n\n\n')
    print('\t \t    UP\n')
    print(f'\t{board[0]}')
    print(f'\t{board[1]}')
    print(f'\t{board[2]}')
    print(f'LEFT    {board[3]}    RIGHT')
    print(f'\t{board[4]}')
    print(f'\t{board[5]}')
    print(f'\t{board[6]}')
    print('\n')
    print('\t \t   DOWN\n')
    print(' ')
    
get_frame()

#Get the coordinates of a character
def get_coord(name):
    global board
    character = characters.get(name)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == character: 
                return [i,j]
    
#Get the name of a character based on its coordinates
def get_name(Coord):
    global board
    nombre = board[Coord[0]][board[0][1]]
    return[nombre]

#Move a character up
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

#Move a character down
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

#Move a character left
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

#Move a character right
def move_right(Player):
    global board
    coord = get_coord(Player)
    
    if coord[1] >= len(board[0]) - 1: 
        dest_col =0
    else:
        dest_col = coord[1] + 1

    if board[coord[0]][dest_col] == None:
        board[coord[0]][dest_col] = board[coord[0]][coord[1]]
        board[coord[0]][coord[1]] = None
    
    get_frame()
        


while winner == None:
    
    # Ask for player and move
    if turn == 'Blue team':
        print('\n' + turn + ' turn')
        print('B1 for: ' + characters['B1'] + '\t' + 'B2 for: ' +characters['B2'])
        player = 'B' + input('Player: B')
        
        while player not in BLUE_TEAM:
            print("Invalid player")
            print('B1 for: ' + characters['B1'] + '\t' + 'B2 for: ' +characters['B2'])
            player = 'B' + input('Player: B')
        
        move = input('Move (up, right, left, down): ')
        while move not in ['up','down','left','right']:
            print("Invalid move")
            move = input('Move (up, right, left, down): ')    
    else:
        print('\n' + turn + ' turn')
        print('R1 for: ' + characters['R1'] + '\t' + 'R2 for: ' +characters['R2'])
        player = 'R' + input('Player: R')
        
        while player not in RED_TEAM:
            print('R1 for: ' + characters['R1'] + '\t' + 'R2 for: ' +characters['R2'])
            print("Invalid player")
            player = 'R' + input('Player: R')
        
        move = input('Move (up, right, left, down): ')
        while move not in ['up','down','left','right']:
            print("Invalid move")
            move = input('Move (up, right, left, down): ')

    # Move player
    if move=='up':
        move_up(player)
    elif move=='down':
        move_down(player)
    elif move == ('left'):
        move_left(player)
    elif move == ('right'):
        move_right(player)
    
    # Check winner
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