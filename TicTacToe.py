def print_board(board):     #function to print the Tic Tac Toe Board
    print("|"+board[0]+"|"+board[1]+"|"+board[2]+"|")
    print("|"+board[3]+"|"+board[4]+"|"+board[5]+"|")
    print("|"+board[6]+"|"+board[7]+"|"+board[8]+"|")

def input_data():
    result="y"                  #To check if user wants to start a new game
    check_board=False
    while result=="y":
        board=["0","1","2","3","4","5","6","7","8"]
        print("We have two symbols- X and O. We'll start with X")
        turn="X"
        print_board(board)
        while True:
            result="n"
            print("Please enter the desired location")
            try:
                location= int(input())
            except ValueError:
                print("invalid entry")
            if 0 <= location < 9:                           #To check if the index value cross the
                                                            #limit of Board index value
                if board[location] not in ["X","O"]:        #To check if user enters value to an
                                                            #already filled location
                    board[location]=turn
                    print_board(board)
                    turn= "O" if turn== "X" else "X"        #Shifting players
                    if board[0]==board[1]==board[2]:        #Checking for win
                        result=input("You won, do you want to continue playing(y/n)")
                        break
                    elif board[3]==board[4]==board[5]:
                        result=input("You won, do you want to continue playing(y/n)")
                        break
                    elif board[6]==board[7]==board[8]:
                        result=input("You won, do you want to continue playing(y/n)")
                        break
                    elif board[0]==board[3]==board[6]:
                        result=input("You won, do you want to continue playing(y/n)")
                        break
                    elif board[1]==board[4]==board[7]:
                        result=input("You won, do you want to continue playing(y/n)")
                        break
                    elif board[2]==board[5]==board[8]:
                        result=input("You won, do you want to continue playing(y/n)")
                        break
                    elif board[0]==board[4]==board[8]:
                        result=input("You won, do you want to continue playing(y/n)")
                    elif board[2]==board[4]==board[6]:
                        result=input("You won, do you want to continue playing(y/n)")
                        break
                else:
                    print("Postion already filled, Please choose another position")
            else:
                print("Please enter value between 0 and 9")
            check_board=all([x in ["X","O"] for x in board])        #Checking if all the rows are
                                                                        #filled with "X" or "0"(Tie)
            if check_board:
                result=input("Box filled completely, do you want to start over")
                break
        if result=='n':
            break
if __name__ == "__main__":
    input_data()
