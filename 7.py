'''
SATART.
TAKE THE USER INPUT ON x OR o DSIPLAY THE BOARD AND CALCULATE WINNER
TAKE INPUT HOW()
FIRST ASK THE USR TO ENTER A NUMBER BETWEEN 0 TO 8 AND IF THAT IS INVALID TRY AGAIN FROM THE USER
DISPLAYING USERS INPUT IN THE BOARD??
---------------------------------------------FIRS TKAE THE INPUT NAD PRITN AFTER EACH MOVE THEN TAKE THAT INPUT AND GIVE IT A INDEX IN BOARD'''
        # I WANT TO DISPLAY USERS INPUT IN THE BOARD HOW.
'''
        FIRST. TAKE THE USER INPUT AND GIVE IT A POSITION IN THE BOARD 
        HOW TO CONVERT USER INPUT INTO A STR AND PLACE IT IN THE BOARDD
        HOW TO CONVERT TO A STR>
        take the user input and make it a str
        NOW GIVE A POSITION TO X IN BOARD                            
'''
'''
        '''
        # I WANT TO MAKE A COMBIANTION OF WINING PATTERS
        # HOW. 
        # MAKE A LSIT AND INSIDE TUPLES OF WINING COMBINATIONS
        #         # '''
        # I HAVE TO AKE THE BAORD CONSTANT RATHER THAN CHNGING DUE TO THE WHILE LOOP FIXED✅✅

        # I HAVE TO DECLARE THE WINNERR 
        # HOW.
        # FIRST MAKE A WINNING COMBINATIONS OUTSIDE THE LOOP SO IT DOESNT CHANGES EVERY TIME


        # CHECK WHO WON 
        # CHECKS DRAW
        # WHO WON HOW.
        # first make winning combinations
        # THEN CHECK IF THE USERS INPUTS HAVE SATISFED THE COMBO ELSE PRINT ITS A DRAW 
'''

def boardd():
    board = [" "] * 9

    while 2 > 1:
        X = int(input("X's turn (0-8) 10 to quit: "))
        if X == 10:
            print("OK BYE")
            break
        if X > 8:
            print("too high: ")
            continue
        if X < 0:
            print("too low! try again!: ")
            continue
        board[X] = "X" #board is the set of str and in that i am assinging X value index to be the str X instaed of an empty space
        print(board[0] ,  "|" , board [1] ,  "|" , board[2] , "|" )
        print("--------------")
        print(board[3] ,  "|" , board[4] , "|" , board[5] , "|" )
        print("--------------")
        print(board[6] ,  "|" , board[7] ,  "|" , board[8] , "|" )

        if (board[0] == board[1] == board[2] != " " or
           board[3] == board[4] == board[5] != " " or
           board[6] == board[7] == board[8] != " " or
           board[0] == board[3] == board[6] != " " or
           board[1] == board[4] == board[7] != " " or
           board[2] == board[5] == board[8] != " " or
           board[0] == board[4] == board[8] != " " or
           board[2] == board[4] == board[6] != " " ):
           print("X WINS!")
           break

        O = int(input("O's turn enter a number (0-8) 10 to quit"))
        if O == 10:
                print("OK")
                break  
        if O > 8:
                print("too high: ")
                continue
        if O < 0:
                print("too low!: ")
                continue

        board[O] = "O"
        print(board[0] , "|" , board[1] , "|" , board[2] , "|" )
        print("--------------")
        print(board[3] , "|" , board[4] , "|" , board[5] , "|" )
        print("--------------")
        print(board[6] , "|" , board[7] , "|" , board[8] , "|" )

        if (board[0] == board[1] == board[2] != " " or
           board[3] == board[4] == board[5] != " " or
           board[6] == board[7] == board[8] != " " or
           board[0] == board[3] == board[6] != " " or
           board[1] == board[4] == board[7] != " " or
           board[2] == board[5] == board[8] != " " or
           board[0] == board[4] == board[8] != " " or
           board[2] == board[4] == board[6] != " " ):
           print("O WINS!")
           break
boardd()

