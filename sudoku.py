import random
import copy

def printboard(board):
    rownum = 0
    for row in board:
        rownum += 1
        prow = ""
        index = 1
        for num in row:
            if index == 3 or index == 6:
                prow += (str(num) + " | " )
            else: prow += str(num) + " "
            
            index = index+1
        print(prow)
        if rownum == 3 or rownum == 6:
            print("---------------------")

def generateboard():
    grid = []
    for i in range(0,9):
        listi = []
        grid.append(listi)

    for row in grid:
        for i in range(0,9):
            row.append(random.randint(1, 9))
    for row in grid:
        random.shuffle(row)
    #print("Generated a random board")
    return(grid)

def validaterow(row):
    for i in range(0, 9):
            num = row[i]
            if row[i] != 0:
                for j in range(i,9):
                    if row[i] == row[j] and j > i:
                        row[j] =0
    return(row)
    
def makesections(grid, x, y):
    minirow=[]
    sec = []
    for i in range(x,(x+3)):
        row = grid[i]
        minirow = row[y:(y+3)]
        if len(sec) < 3:
            sec.append(minirow)
    return(sec)

def validatesections(sections):
    #print("unvalidated sections")
    #print(sections)
    newsec = []
    for sec in sections:
        list = []
        for x in range(0,3):
            for y in range(0,3):
                list.append(sec[x][y])
        #print("unvalidated list", list)
        list = validaterow(list)
        trisection = []
        trisection.append(list[0:3])
        trisection.append(list[3:6])
        trisection.append(list[6:9])
        #print(list)
        #print(trisection)
        newsec.append(trisection)
    #print("sections validated")
    #print(newsec)
    #print(sections)
    return(newsec)
    
def desection(sections):
    rows = []
    for i in range(0,9):
        rows.append([])
    
    for i in [0,3,6]:
        for x in range(0,3):
            for num in sections[x+i][0]: rows[i].append(num)
            for num in sections[x+i][1]: rows[i+1].append(num)
            for num in sections[x+i][2]: rows[i+2].append(num)
    #printboard(rows)
    return(rows)
    
def makevalid(grid):
    rowcount = 0
    for row in grid:    # Delete any duplicate numbers from rows
        grid[rowcount] = validaterow(row)
        rowcount = rowcount + 1
        
    for colnum in range(0,9): # Delete any duplicate numbers from columns
        for rownum in range(0,9):
            num = grid[rownum][colnum]
            for i in range((rownum + 1), 9):
                if grid[rownum][colnum] == grid[i][colnum] and grid[rownum][colnum] != 0:
                    #print(grid[i][colnum])
                    #print("got one, row", rownum, "column", i, "was", grid[rownum][i], "is now 0")
                    grid[i][colnum] = 0
    #printboard(grid)
    #print("xxxxxxxxxxxxxxxxxxxxxxxx")
    sections = [] # create sections
    for x in[0, 3, 6]:
        for y in[0, 3, 6]:
            sections.append(makesections(grid,x,y))
            
    newsec = validatesections(sections)
    #print(" Newsec AFTER validating")
    #print(newsec)
    grid = desection(newsec)
    
    return(grid)


'''
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]'''


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0
        

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

'''
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")'''


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None


board = []
goagain = True
while goagain == True:
    
    board = generateboard()
    
    board = makevalid(board) 
    # for some reason, I can't have a seperate unsolved and solved board
    unsolved = []
    unsolved = copy.deepcopy(board)
    
    #printboard(unsolved)
    #print("==============")
    
    solve(board)
    
    goagain = False
    for row in board:
        for number in row:
            if number == 0:
                goagain = True

printboard(unsolved)
print("")
print("=======================")
print("")
printboard(board)


'''
board = generateboard()
unsolved = board
board = makevalid(board)
printboard(board)



grid = generateboard()


grid = makevalid(grid)
#print(grid)
printboard(grid)

'''
