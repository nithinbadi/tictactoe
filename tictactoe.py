import os
def draw_board(x):
    os.system('cls')
    print('    |     |    ')
    print(f' {x[0]}  |  {x[1]}  |  {x[2]} ')
    print('    |     |    ')
    print("---------------")
    print('    |     |    ')
    print(f' {x[3]}  |  {x[4]}  |  {x[5]} ')
    print('    |     |    ')
    print("---------------")
    print('    |     |    ')
    print(f' {x[6]}  |  {x[7]}  |  {x[8]} ')
    print('    |     |    ')


def check_winner(x,p):
    if (x[0]==p and x[1]==p and x[2]==p) or (x[3]==p and x[4]==p and x[5]==p) or (x[6]==p and x[7]==p and x[8]==p):
        return True
    elif (x[0]==p and x[3]==p and x[6]==p) or (x[1]==p and x[4]==p and x[7]==p) or (x[2]==p and x[5]==p and x[8]==p):
        return True
    elif (x[0]==p and x[4]==p and x[8]==p) or (x[2]==p and x[4]==p and x[6]==p):
        return True
    return False


initial_board=[" "," "," ",
               " "," "," ",
               " "," "," "]

#dummy_board = ["1","2","3","4","5","6","7","8","9"]


player="X"

#game loop

while True:
    board_full=all([i!=" " for i in initial_board])
    draw_board(initial_board)
    if check_winner(initial_board,"X"):
        print("X is the winner")
        break
    elif check_winner(initial_board,"O"):
        print("O is the winner")
        break
    elif board_full:
        print("Draw")
        break
    while not board_full:
        player_choice=input("Enter position[1-9]: ")
        if player_choice.isdigit() and int(player_choice) in list(range(1,10)):
            if initial_board[int(player_choice)-1] == " ":
                initial_board[int(player_choice)-1]=player
                if player=="X":    
                    player="O"
                else:
                    player="X"
                break
            else:
                print("Position taken. try another position")
        else:
            print("Not a valid position. Try again")