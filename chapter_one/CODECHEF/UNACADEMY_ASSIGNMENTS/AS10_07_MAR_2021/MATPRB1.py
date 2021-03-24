# symmetric check
def symmetric(matrix, len):
    for i in range(len):
        for j in range(len):
            if (matrix[i][j] != matrix[j][i]):
                return False
    return True

# triangular check = if lower or upper, it should considered
def lowertriangular(em):
    for i in range(0, len(em)):
        for j in range(i + 1, len(em)):
            if(em[i][j] != 0):
                    return False
    return True

def uppertriangular(em):
    for i in range(1, len(em)):
        for j in range(0, i):
            if(em[i][j] != 0):
                    return False
    return True

# check diagonal
def diagonal(go, en) :
    for i in range(0, en):
        for j in range(0, en) :

            if ((i != j) and
             (go[i][j] != 0)) :
                return False

    return True

T = int(input())
for x in range(0, T):
    c = int(input())
    if c < 1:
        exit()
    matrix = []
    for x in range(c):
        li = [int(x) for x in input().split()]
        matrix.append(li)
    s = t = d = 0

    if (symmetric(matrix,len(matrix))): # symmetric call
        s = 1

    if uppertriangular(matrix) or lowertriangular(matrix): # triangular call
        t = 1

    if diagonal(go, c): # diagonal call
        d = 1
    print(s+2*t+4*d)
