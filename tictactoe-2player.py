def newBoard():
    initBoard = [[' ']*3 for i in range(3)]
    return initBoard
def renderBoard(board):
    # Render the board
    horizNums = ''
    horizLine = ''
    
    for i in range(3):
        horizNums += str(i) + ' '
        horizLine += '- '
    print("",horizNums)
    print("", horizLine)
    vert = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if j == 0:
                print("|", end = '')
            if j == len(board[0])-1:
                print(board[i][j], end = "")
                print("|" + str(vert), end = "")
                vert +=1
            else:
                if j != len(board[0])-1:
                    print(board[i][j], end = " ")
                else:
                    print(board[i][j])
        print("\t")
    print("", horizLine)
    
def getMove():
    playerX = int(input("Enter row: "))
    playerY = int(input("Enter col: "))
    
    
    return (playerX, playerY)

def makeMove(board, moveCoords, player1 = True):
    # Make a new board with the given board, 
    # and input the player's move coordinates depending on if they are player1
    # or player 2. Then return the new board.
    while True:
        try:
            newBoard = board
            if isValid(moveCoords, newBoard):
                if player1 is True:
                    newBoard[moveCoords[0]][moveCoords[1]] = 'x'
                else:
                    newBoard[moveCoords[0]][moveCoords[1]] = 'o'
                return newBoard
            else:
                while not isValid(moveCoords, newBoard):
                    print("Invalid move -- try again")
                    moveCoords = getMove()
                if player1 is True:
                    newBoard[moveCoords[0]][moveCoords[1]] = 'x'
                else:
                    newBoard[moveCoords[0]][moveCoords[1]] = 'o'
                return newBoard
        except:
            print("Invalid coordinates -- try again")
            moveCoords = getMove()

def isValid(move, board):
        if board[move[0]][move[1]] != ' ':
            return False
        return True

def getWinner(board):
    boardList = []
    #Add all horizontal rows to the list
    for i in range(len(board)):
        boardList.append(board[i])
    
    j = 0
    #Add all columns to the list
    for n in range(len(board)): 
        colList = []
        for i in range(len(board)): 
            colList.append(board[i][j])
        j +=1
        boardList.append(colList)
        
    
    #Add first diagonal to the list    
    diagList = []
    for i in range(len(board)):
        for j in range(len(board)):
            if i == j:
                diagList.append(board[i][j])
    boardList.append(diagList)
    
    diagList = []
    #Add second diagonal to the list
    i = 0
    j = 2
    while (i <= 2):
        diagList.append(board[i][j])
        i+=1
        j-=1
    boardList.append(diagList)  
    
    for listele in boardList:
        allsame = True
        for i in range(len(listele)):
            compare = listele[0]

            if listele[i] != compare:
                allsame = False
        if allsame == True:
            if compare == 'x' or compare == 'o':
                return(compare)
    return None
    
def runGame():
    #Creating the board
    x = newBoard()
    renderBoard(x)
    # First play
    player1 = True
    print("Player 1's turn.")
    nextMove = makeMove(x, getMove(), player1)
    renderBoard(nextMove)
    while (getWinner(nextMove) == None):
        player1 = not player1
        if player1 is True:
            print("Player 1's turn.")
        else:
            print("Player 2's turn.")
        nextMove = makeMove(x, getMove(), player1)
        renderBoard(nextMove)
        winner = getWinner(nextMove)
        if isBoardFull(nextMove):
            print("Draw.")
            break  
    if winner == 'x':
        print('Player 1 wins!')
    elif winner == 'o':
        print('Player 2 wins!')   
def isBoardFull(board):
    isFull = True
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ' ':
                return False
    return True

    

runGame()