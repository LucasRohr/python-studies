mat = [ 
    [ 0, 0, 0 ],
    [ 0, 0, 0 ],
    [ 0, 0, 0 ]
 ]

playerOneScore = 0
playerTwoScore = 0

combinations = [
    [ 
        [ 1, 1, 1 ],
        [ 0, 0, 0 ],
        [ 0, 0, 0 ]
    ],

    [ 
        [ 0, 0, 0 ],
        [ 1, 1, 1 ],
        [ 0, 0, 0 ]
    ],

    [ 
        [ 0, 0, 0 ],
        [ 0, 0, 0 ],
        [ 1, 1, 1 ]
    ],

     [ 
        [ 1, 0, 0 ],
        [ 1, 0, 0 ],
        [ 1, 0, 0 ]
    ],

    [ 
        [ 0, 1, 0 ],
        [ 0, 1, 0 ],
        [ 0, 1, 0 ]
    ],

    [ 
        [ 0, 0, 1 ],
        [ 0, 0, 1 ],
        [ 0, 0, 1 ]
    ],

    [ 
        [ 1, 0, 0 ],
        [ 0, 1, 0 ],
        [ 0, 0, 1 ]
    ],

    [ 
        [ 0, 0, 1 ],
        [ 0, 1, 0 ],
        [ 1, 0, 0 ]
    ]
]

def printBoard():
    print(f'{mat[0, 0]} | {mat[0, 1]} | {mat[0, 2]}')
    print('-------------------------------')
    print(f'{mat[1, 0]} | {mat[1, 1]} | {mat[1, 2]}')
    print('-------------------------------')
    print(f'{mat[2, 0]} | {mat[2, 1]} | {mat[2, 2]}')

def checkGameOver():
    if (mat in combinations):
        bestScore = playerOneScore > playerTwoScore and playerOneScore or playerTwoScore
        winnerMessage = bestScore == playerOneScore and 'Player 1 ganhou!' or 'Player 2 ganhou!'
        print('Game Over!')
        playerOneScore = 0
        playerTwoScore = 0
        print(winnerMessage)

def givePointToPlayer(player):
    if(player == 1):
        playerOneScore += 1
    else:
        playerTwoScore += 1

def givePoint(place, player):
    firstRow = [ 7, 8, 9 ]
    secondRow = [ 4, 5, 6 ]
    lastRow = [ 1, 2, 3 ]

    givePointToPlayer(player)

    if(place in firstRow):
        mat[0][place - 7] = 1

    elif(place in secondRow):
        mat[1][place - 4] = 1

    else:
        mat[2][place - 1] = 1

def startGame():

    print(playerOneScore)

    playerOneSymbol = input('Player 1, você quer se X ou O?\n')
    playerTwoSymbol = playerOneSymbol == 'X' and 'O' or 'X'

    while(mat not in combinations):
        attackPlace = int(input('Player 1, sua vez:\n'))
        givePoint(attackPlace, 1)
        checkGameOver()
        printBoard()

        attackPlace = int(input('Player 2, sua vez:\n'))
        givePoint(attackPlace, 2)
        checkGameOver()
        printBoard()

startGame()
