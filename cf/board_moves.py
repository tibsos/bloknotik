t = int(input())

for i in range(t):

    moves = 0

    n = int(input())

    # n x n board
    # theres a piece in every x and y 
    # move all pieces into cell x1 y1 (top left)

    # bottom right number of moves to go = 3

    if n > 0:



        for i in range(1, n):

            if n > 1:

                moves += (n*2-1) * (n-1)

        print(moves)

    else:

        print(0)