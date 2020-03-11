# board = [-1] * 9
# 1 -> cross 
# 0 -> circle

def checkFree(ind1, ind2, board):
    if(board[ind1]==-1 and board[ind2]==-1):
        return True
    else:
        return False

def checkBlocked(ind1, ind2, ind3, value, board):
    if(board[ind1]==value and board[ind2]==value):
        return ind3
    elif(board[ind2]==value and board[ind3]==value):
        return ind1
    elif(board[ind1]==value and board[ind3]==value):
        return ind2
    else:
        return -1

def checkBetween(value, board):
    if checkBlocked(0, 1, 2, value, board) != -1:
        return checkBlocked(0, 1, 2, value, board)
    elif checkBlocked(3, 4, 5, value, board) != -1:
        return checkBlocked(3, 4, 5, value, board)
    elif checkBlocked(6, 7, 8, value, board) != -1:
        return checkBlocked(6, 7, 8, value, board)
    elif checkBlocked(0, 3, 6, value, board) != -1:
        return checkBlocked(0, 3, 6, value, board)
    elif checkBlocked(1, 4, 7, value, board) != -1:
        return checkBlocked(1, 4, 7, value, board)
    elif checkBlocked(2, 5, 8, value, board) != -1:
        return checkBlocked(2, 5, 8, value, board)
    elif checkBlocked(2, 5, 8, value, board) != -1:
        return checkBlocked(2, 5, 8, value, board)
    elif checkBlocked(0, 4, 8, value, board) != -1:
        return checkBlocked(0, 4, 8, value, board)
    elif checkBlocked(2, 4, 6, value, board) != -1:
        return checkBlocked(2, 4, 6, value, board)
    else: 
        return -1
    


def compMove(moves, board):
    if(moves == 0):
        return 8
    elif moves == 1:
        if(board[4]==-1):
            return 4 
        else:
            return 8
    elif moves == 2:
        if(board[4]==-1):
            return 4 
        else:
            return 8
    elif moves == 3:
        val = checkBetween(1, board)
        if val != -1:
            if(board[val] == -1):
                return val
        if checkFree(1, 7, board):
            return 7
        elif checkFree(3, 5, board):
            return 3
        else:
            for ind in range(9):
                if(board[ind]==-1):
                    return ind
    elif moves == 4:
        pass 
    elif moves >= 5:
        val = checkBetween(1, board)
        # print('val=>', val)
        if val != -1:
            if(board[val] == -1):
                return val
        for ind in range(9):
            if(board[ind]==-1):
                return ind


