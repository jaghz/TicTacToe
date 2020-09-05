import random
import copy

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

    if player1 is True:
        board[moveCoords[0]][moveCoords[1]] = 'x'
    else:
        board[moveCoords[0]][moveCoords[1]] = 'o'
    return board

        



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
            if listele[i] == 'o ' or listele[i] == ' o' or listele[i] == ' o ':
                listele[i] = 'o'
            if listele[i] == 'x ' or listele[i] == ' x' or listele[i] == ' x ':
                listele[i] = 'x'
            compare = listele[0]

            if listele[i] != compare:
                allsame = False

        if allsame == True:
            if compare == 'x' or compare == 'o':

                return(compare)
    #print(boardList)
    return None

def isBoardFull(board):
    isFull = True
    #print(board)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ' ':
                return False
    return True
    
def isTerminal(board):
    winner = getWinner(board)

    if winner == 'x':
        return(10)
    elif winner == 'o':
        return(-10)
    elif isBoardFull(board):
        return(0)
    return None
   
def possibleMoves(board):
    possibleMoves=[]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == ' ':
                possibleMoves.append((i,j))
    return(possibleMoves)
board = [['o', 'o', ' '],[' ', 'x', 'x'],['x', ' ', ' ']]
def miniMax(board, player1):
    #base case:
    if isTerminal(board) is not None:

        return isTerminal(board)
    scores = []

    for move in possibleMoves(board):
        newBoard = copy.deepcopy(board)

        nextMove = makeMove(newBoard, move, player1)

        score = miniMax(nextMove, not player1)
        scores.append(score)

    if player1 == True:
        return(max(scores))
    else:
        return(min(scores))
   
     
def perfectAI(board, player1=False):
    moves = possibleMoves(board)

    bestScore = None
    bestMove=None
    
    for move in moves:
        newBoard = copy.deepcopy(board)

        moveScore = miniMax(newBoard, player1)
        if bestScore is None or moveScore < bestScore:
            bestMove = move
            bestScore = moveScore
    return bestMove

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
        #print(player1)
        if player1 is True:
            print("Player 1's turn.")
            nextMove = makeMove(x, getMove(), player1)
            renderBoard(nextMove)
            winner = getWinner(nextMove)
        else:
            print("Player 2's turn.")
            print("Thinking...")
            nextMove = makeMove(x, perfectAI(nextMove), player1)
            renderBoard(nextMove)
            winner = getWinner(nextMove)
            
        if isBoardFull(nextMove):
            print("Draw.")
            break  
    if winner == 'x':
        print('Player 1 wins!')
    elif winner == 'o':
        print('Player 2 wins!')   

runGame()
