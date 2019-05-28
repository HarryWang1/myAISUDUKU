import time 
from CSP import csp
from Backtrack import *

clean = []
with open('SUDUKO_Input5.txt') as f: #path
    for line in f:
    	for num in line:
    		if num.isdigit():
		        clean.append(num)
grid = "".join(clean)

assert len(grid) == 81
start = time.time()
sudoku = csp(grid=grid)
solved = Backtracking_Search(sudoku)

f = open("SUDUKU_Output5.txt", "a") #path

if solved!="FAILURE":
    display(solved) 		#DISPLAY IN SUDUKU FOMAT
    output = get_Result(solved)
    #WRTIE TO OUTPUT TXT
    for row in output:
        f.write(" ".join(row))
        f.write("\n")

    f.close()

    print ("This puzzle was solved in: ", time.time()-start," seconds")
    print ("Perfectly solved")
else:
	print ("Not solved")

f.close()
