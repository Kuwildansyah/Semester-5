import random

def generate_board(size):
    return [[' ' for _ in range(size)] for _ in range(size)]
 
x = lambda size:[[' ' for _ in range(size)] for _ in range(size)]

x(10)

def generate_positions(size):
    return (random.randint(0, size-1), random.randint(0, size-1))

def print_board(board, player_pos, goal_pos):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (i, j) == player_pos:
                print('A', end=' ')
            elif (i, j) == goal_pos:
                print('O', end=' ')
            else:
                print(board[i][j], end=' ')
        print()


def move_player(board, player_pos, direction):
    if direction == 'w':
        return max(0, player_pos[0] - 1), player_pos[1]
    elif direction == 's':
        return min(len(board) - 1, player_pos[0] + 1), player_pos[1]
    elif direction == 'a':
        return player_pos[0], max(0, player_pos[1] - 1)
    elif direction == 'd':
        return player_pos[0], min(len(board) - 1, player_pos[1] + 1)
    else:
        return player_pos

def play_game(size):
    board = x(size)
    player_pos = generate_positions(size)
    goal_pos = generate_positions(size)
    
    # Mastiin goal sama player tidak berdempetan
    while abs(goal_pos[0] - player_pos[0]) + abs(goal_pos[1] - player_pos[1]) < size // 2 or goal_pos == player_pos:
        goal_pos = generate_positions(size)
    
    move_counter = 0
    while True:
        print_board(board, player_pos, goal_pos)
        direction = input("Move your player (A) (w/a/s/d): ")
        player_pos = move_player(board, player_pos, direction)
        
        move_counter += 1
        if move_counter == 3:
            if player_pos == goal_pos:
                print("Ngeri Sepuh!")
                break
            else:
                goal_pos = generate_positions(size)
                while abs(goal_pos[0] - player_pos[0]) + abs(goal_pos[1] - player_pos[1]) < size // 2 or goal_pos == player_pos:
                    goal_pos = generate_positions(size)
                move_counter = 0
        
        if player_pos == goal_pos:
            print("Anjay Pro Peler!")
            break

play_game(5)
