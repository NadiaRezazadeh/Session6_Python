def show():
    for row in game_board:
        for cell in row:
            print(cell,"",end="")
        print()


game_board = [["-","-","-"],
              ["-","-","-"],
              ["-","-","-"]]

while True:

    print("player1")
    while True:
        row = int(input("Enter row number(between 0 and 2) :"))              
        col = int(input("Enter column number(between 0 and 2) :"))
        if 0 <= row <= 2 and 0<= col <= 2:
            if game_board[row][col] == "-":
                game_board[row][col] = "x"
                show()
                break
            else:
                print("Choose another one :")
                continue

    if game_board[0][0] == "x" and game_board[0][1] == "x" and game_board[0][2] == "x":
        print("player1 won!!")
        break 
    elif game_board[1][0] == "x" and game_board[1][1] == "x" and game_board[1][2] == "x":
        print("player1 won!!")
        break
    elif game_board[2][0] == "x" and game_board[2][1] == "x" and game_board[2][2] == "x":
        print("player1 won!!")
        break
    elif game_board[0][0] == "x" and game_board[1][0] == "x" and game_board[2][0] == "x":
        print("player1 won!!")
        break
    elif game_board[0][1] == "x" and game_board[1][1] == "x" and game_board[2][1] == "x":
        print("player1 won!!")
        break
    elif game_board[0][2] == "x" and game_board[1][2] == "x" and game_board[2][2] == "x":
        print("player1 won!!") 
        break
    elif game_board[0][0] == "x" and game_board[1][1] == "x" and game_board[2][2] == "x":
        print("player1 won!!") 
        break
    elif game_board[0][2] == "x" and game_board[1][1] == "x" and game_board[2][0] == "x":
        print("player1 won!!") 
        break
    if game_board[0][0] != "-" and game_board[0][1] != "-"and game_board[0][2] != "-"and game_board[1][0]!= "-" and game_board[1][1]!= "-" and game_board[1][2]!= "-" and game_board[2][0]!= "-"and game_board[2][1]!= "-"and game_board[2][2]!= "-":
        print("Draw!!")
        break

    else:
        print("player2")
        while True:
            row = int(input("Enter row number(between 0 and 2) :"))              
            col = int(input("Enter column number(between 0 and 2) :"))
            if 0 <= row <= 2 and 0<= col <= 2:
                if game_board[row][col] == "-":
                    game_board[row][col] = "o"
                    show()
                    break
                else:
                    print("Choose another one :")
                    continue
    if game_board[0][0] == "o" and game_board[0][1] == "o" and game_board[0][2] == "o":
            print("player2 won!!") 
            break
    elif game_board[1][0] == "o" and game_board[1][1] == "o" and game_board[1][2] == "o":
        print("player2 won!!")
        break 
    elif game_board[2][0] == "o" and game_board[2][1] == "o" and game_board[2][2] == "o":
        print("player2 won!!") 
        break  
    elif game_board[0][0] == "o" and game_board[1][0] == "o" and game_board[2][0] == "o":
        print("player2 won!!") 
        break
    elif game_board[0][1] == "o" and game_board[1][1] == "o" and game_board[2][1] == "o":
        print("player2 won!!") 
        break
    elif game_board[0][2] == "o" and game_board[1][2] == "o" and game_board[2][2] == "o":
        print("player2 won!!") 
        break
    elif game_board[0][0] == "o" and game_board[1][1] == "o" and game_board[2][2] == "o":
        print("player2 won!!")       
        break
    elif game_board[0][2] == "o" and game_board[1][1] == "o" and game_board[2][0] == "o":
        print("player2 won!!") 
        break     