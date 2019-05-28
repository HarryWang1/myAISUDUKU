from CSP import *
from copy import deepcopy

def Backtracking_Search(csp):
	return Backtrack({}, csp)

def Backtrack(assignment, csp):
	if isComplete(assignment):
		return assignment

	var = Select_Unassigned_Variables(assignment, csp)
	domain = deepcopy(csp.values)

	for value in csp.values[var]:
		if isConsistent(var, value, assignment, csp):
			assignment[var] = value
			inferences = {}
			inferences = Inference(assignment, inferences, csp, var, value)
			if inferences!= "FAILURE":
				result = Backtrack(assignment, csp)
				if result!="FAILURE":
					return result

			del assignment[var]
			csp.values.update(domain)

	return "FAILURE"


def forward_check(csp, assignment, var, value):
	csp.values[var] = value
	for neighbor in csp.peers[var]:
		csp.values[neighbor] = csp.values[neighbor].replace(value, '')


#FORWARD CHECKING WITH INFERENCES
def Inference(assignment, inferences, csp, var, value):
	inferences[var] = value

	for neighbor in csp.peers[var]:
		if neighbor not in assignment and value in get_Neighbors(neighbor,csp):
			if len(get_Neighbors(neighbor,csp))==1:
				return "FAILURE"
			forward_check(csp, assignment, var, value)
			if len(csp.values[neighbor])==1:
				flag = Inference(assignment, inferences, csp, neighbor, get_Neighbors(neighbor,csp))
				if flag=="FAILURE":
					return "FAILURE"

	return inferences

			
#CHECKS ASSIGNMENT
def isComplete(assignment):
	return set(assignment.keys())==set(squares)


def Select_Unassigned_Variables(assignment, csp): #with MRV
	unassigned_variables = dict((squares, len(csp.values[squares])) for squares in csp.values if squares not in assignment.keys())

	mrv = min(unassigned_variables, key=unassigned_variables.get)
	return mrv

def Order_Domain_Values(var, csp):
	return csp.values[var]

def get_Neighbors(var,csp):
	return csp.values[var]

#CHECKS IF THE GIVEN NEW ASSIGNMENT IS CONSISTENT
def isConsistent(var, value, assignment, csp):
	for neighbor in Order_Domain_Values(var, csp):
		if neighbor in assignment.keys() and assignment[neighbor] == value:
			return False
	return True


def display(result):
    for r in rows:
    	if r in 'DG':
    		print ("----------------------------------------------")
    	for c in cols:
    		if c in '47':
    			print (' | ', result[r+c], ' ',end=' ')
    		else:
    			print (result[r+c], ' ',end=' ')
    	print (end='\n')

def get_Result(values):
	output = ""
	for variable in squares:
		output = output + values[variable]
	i = 0
	result = []
	while i < 9:
		result.append([output[i:i+9]])
		i += 1

	return result
