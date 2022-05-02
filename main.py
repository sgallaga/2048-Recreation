from utilities import generate_piece, print_board

DEV_MODE = False


def main(game_board: [[int, ], ]) -> [[int, ], ]:
    """
    2048 main function, runs a game of 2048 in the console.

    Uses the following keys:
    w - shift up
    a - shift left
    s - shift down
    d - shift right
    q - ends the game and returns control of the console
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: returns the ending game board
    """
    # 
    # TODO: generate a random piece and location using the generate_piece function
    
    put_piece(game_board)
    
    # TODO: place the piece at the specified location
    # Initialize game state trackers
    game_won = False
    game_lost = False
    comps_turn = True
    user_input = ''
    

    # Game Loop
    #while (not (game_won)) or (not (game_lost)) or (user_input != 'q'):
    while not game_won and not game_lost and user_input != 'q':
        # TODO: Reset user input variable
        user_input = ''
        
        # TODO: Take computer's turn
        # place a random piece on the board
        # check to see if the game is over using the game_over function
        
        if comps_turn:
            put_piece(game_board)
            
            if game_over(game_board):
                game_lost = True
                print("G A M E  O V E R")
                print_board(game_board)
                break
            
            else:
                comps_turn = False
                    
        
        # TODO: Show updated board using the print_board function
        print_board(game_board)
        
        # TODO: Take user's turn
        # Take input until the user's move is a valid key
        # if the user quits the game, print Goodbye and stop the Game Loop
        # Execute the user's move
        if not comps_turn:
            
            valid_move = False
            
            while not valid_move:
                user_input = input("Your Turn:\n")
                
                while user_input not in ('a','d','w','s','q'):
                    print("Invalid input. Please use one of the following characters \"w\", \"a\", \"s\", \"d\".")
                    user_input = input("Enter again:")
                
                #test for valid shift_left move
                
                if user_input == 'a':
                    fake_list = [[],[],[],[]]
                    for index_r, row in enumerate(game_board):
                        for index_c, cell in enumerate(row):
                            fake_list[index_r].append(cell)
                    
                    shift_left(fake_list)
        
                    for index_r, row in enumerate(fake_list):
                        for index_c, cell in enumerate(row):
                            if cell != game_board[index_r][index_c]:
                                valid_move = True
                                
                    if valid_move == True:
                        shift_left(game_board)
                        break
                        
                #test for valid shift_right move
                
                elif user_input == 'd':
                    
                    fake_list = [[],[],[],[]]
                    for index_r, row in enumerate(game_board):
                        for index_c, cell in enumerate(row):
                            fake_list[index_r].append(cell)
                    
                    shift_right(fake_list)
        
                    for index_r, row in enumerate(fake_list):
                        for index_c, cell in enumerate(row):
                            if cell != game_board[index_r][index_c]:
                                valid_move = True
                                
                    if valid_move == True:
                        shift_right(game_board)
                        break
                
                #test for valid up_move
                
                elif user_input == 'w':
                    fake_list = [[],[],[],[]]
                    for index_r, row in enumerate(game_board):
                        for index_c, cell in enumerate(row):
                            fake_list[index_r].append(cell)
                    
                    shift_up(fake_list)
        
                    for index_r, row in enumerate(fake_list):
                        for index_c, cell in enumerate(row):
                            if cell != game_board[index_r][index_c]:
                                valid_move = True
                                
                    if valid_move == True:
                        shift_up(game_board)
                        break
                    
                    
                elif user_input == 's':
                    fake_list = [[],[],[],[]]
                    for index_r, row in enumerate(game_board):
                        for index_c, cell in enumerate(row):
                            fake_list[index_r].append(cell)
                    
                    shift_down(fake_list)
        
                    for index_r, row in enumerate(fake_list):
                        for index_c, cell in enumerate(row):
                            if cell != game_board[index_r][index_c]:
                                valid_move = True
                                
                    if valid_move == True:
                        shift_down(game_board)
                        break
                    
                elif user_input == 'q':
                    print("Goodbye")
                    break
                
                print("Invalid move")
            
            # Check if the user wins
            for index_r, row in enumerate(game_board):
                for index_c, cell in enumerate(row):
                    if cell == 2048:
                        game_won = True
                        print_board(game_board)
                        print("Congratulations! You've won 2048 :)")
                    
            comps_turn = True
              
    
    return game_board


def game_over(game_board: [[int, ], ]) -> bool:
    """
    Query the provided board's game state.

    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: Boolean indicating if the game is over (True) or not (False)
    """
    # TODO: Loop over the board and determine if the game is over
    
    return not check_valid(game_board)  # TODO: Don't always return false


def put_piece(game_board):
    if DEV_MODE:
        place_piece = generate_piece(game_board, True)
        game_board[place_piece['row']][place_piece['column']] = place_piece['value']
    
    else:
        place_piece = generate_piece(game_board)
        game_board[place_piece['row']][place_piece['column']] = place_piece['value']


def check_valid(game_board):
    fake_list = [[],[],[],[]]
    for index_r, row in enumerate(game_board):
        for index_c, cell in enumerate(row):
            fake_list[index_r].append(cell)
    
    shift_left(fake_list)
    
    for index_r, row in enumerate(fake_list):
        for index_c, cell in enumerate(row):
            if cell != game_board[index_r][index_c]:
                return True
                
    fake_list = [[],[],[],[]]
    for index_r, row in enumerate(game_board):
        for index_c, cell in enumerate(row):
            fake_list[index_r].append(cell)
    
    shift_right(fake_list)
            
    for index_r, row in enumerate(fake_list):
        for index_c, cell in enumerate(row):
            if cell != game_board[index_r][index_c]:
                return True
                
    fake_list = [[],[],[],[]]
    for index_r, row in enumerate(game_board):
        for index_c, cell in enumerate(row):
            fake_list[index_r].append(cell)   
            
    shift_up(fake_list)
            
    for index_r, row in enumerate(fake_list):
        for index_c, cell in enumerate(row):
            if cell != game_board[index_r][index_c]:
                return True
                
    fake_list = [[],[],[],[]]
    for index_r, row in enumerate(game_board):
        for index_c, cell in enumerate(row):
            fake_list[index_r].append(cell)
            
    shift_down(fake_list)
            
    for index_r, row in enumerate(fake_list):
        for index_c, cell in enumerate(row):
            if cell != game_board[index_r][index_c]:
                return True        
            
    return False
    
    
def shift_left(matrix):
    for row in matrix:
        added_list = []
        new_list = [[],[],[],[]]
        for cl_index in range(1,4):
            if row[cl_index] != 0:
                cl_counter = 0
                for adj_index in range(cl_index - 1, -1, -1):
                    f_list = row[:]
                    if f_list[adj_index] == 0:
                        row[adj_index] = row[cl_index + cl_counter]
                        row[cl_index + cl_counter] = 0
                        cl_counter -= 1
                    elif f_list[adj_index] == f_list[cl_index + cl_counter] and adj_index not in added_list:
                        row[adj_index] += row[cl_index + cl_counter]
                        row[cl_index + cl_counter] = 0
                        added_list.append(adj_index)
                        
                        break
                    else:
                        break
                    
                    
def shift_right(matrix):
    for row in matrix:
        added_list = []
        for cl_index in range(3,-1,-1):
            if row[cl_index] != 0:
                cl_counter = 0
                for adj_index in range(cl_index + 1, 4):
                    f_list = row[:]
                    if f_list[adj_index] == 0:
                        row[adj_index] = row[cl_index + cl_counter]
                        row[cl_index + cl_counter] = 0
                        cl_counter += 1
                    elif f_list[adj_index] == f_list[cl_index + cl_counter] and adj_index not in added_list:
                        row[adj_index] += row[cl_index + cl_counter]
                        row[cl_index + cl_counter] = 0
                        added_list.append(adj_index)
                        
                        break
                    else:
                        break
                    
                    
def shift_up(matrix):
    horizontal = [[],[],[],[]]
    for row in matrix:
        for index, column in enumerate(row):
            horizontal[index].append(column)
            
    shift_left(horizontal)
    for index_1, column in enumerate(horizontal):
        for index_2, cell in enumerate(column):
            matrix[index_2][index_1] = cell
            
            
def shift_down(matrix):
    horizontal = [[],[],[],[]]
    for row in matrix:
        for index, column in enumerate(row):
            horizontal[index].append(column)
            
    shift_right(horizontal)
    for index_1, column in enumerate(horizontal):
        for index_2, cell in enumerate(column):
            matrix[index_2][index_1] = cell
            
         

if __name__ == "__main__":
    main([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]) 
          
