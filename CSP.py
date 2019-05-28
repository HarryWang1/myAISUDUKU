digits =  cols = "123456789"
rows = "ABCDEFGHI"

#THE CROSS PRODUCT OF COLS AND ROWS
def crossProduct(A, B):
	return [a + b for a in A for b in B]

global squares 

squares = crossProduct(rows, cols)

#'A1', 'A2', 'A3', 'A4', 'A5', 'A6'.....
#B1 B2 B3 B4


class csp:
	
	#INITIALIZING THE CSP
	def __init__ (self, domain = digits, grid = ""):

		self.variables = squares
		self.domain = self.getDiction(grid)
		self.values = self.getDiction(grid)		

		#Unitlist consists of the 27 lists of peers 

		self.unitlist = ([crossProduct(rows, c) for c in cols] +
            			 [crossProduct(r, cols) for r in rows] +
            			 [crossProduct(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
		##print(self.unitlist)

		#Units is a dictionary consisting of the keys and the corresponding lists of peers 		
		self.units = dict((s, [u for u in self.unitlist if s in u]) for s in squares)
		# print(self.units)

		#Peers is a dictionary consisting of the 81 keys and the corresponding set of 20 peers 
		self.peers = dict((s, set(sum(self.units[s],[]))-set([s])) for s in squares)
		#print(peers)

		#Constraints denote the various all-different constraints between the variables 
		self.constraints = {(variable, peer) for variable in self.variables for peer in self.peers[variable]}




	#GET DICTIONARY BY GRID
	def getDiction(self, grid=""):

		result = dict()
		for i in range(len(self.variables)):
			if grid[i] == '0':
				result[self.variables[i]] = digits
			else:
				result[self.variables[i]] = grid[i]

		return result