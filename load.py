def load_test(path):
	file = open(path,"r")
	content = file.readlines()
	matrix1 = []
	matrix2 = []
	matrix3 = []
	matrix4 = []
	matrix5 = []
	matrix6 = []
	matrix7 = []
	matrix8 = []
	matrix9 = []

	general_matrix = [[i * j for j in range(9)] for i in range(9)]

	for line in content:
		line = line.strip() 
		clean_line = "" # get clean data without space 
		for num in line:
			if num.isdigit():
				clean_line += num
		for i in range(9): 
			for j in range(9):
				general_matrix[i][j] = clean_line[j]


# loading seperate matrix so easier to handle

	matrix1 = general_matrix[0][0:3]+general_matrix[1][0:3]+general_matrix[2][0:3]

	matrix2 = general_matrix[0][3:6] + general_matrix[1][3:6] + general_matrix[2][3:6]

	matrix3 = general_matrix[0][6:9] + general_matrix[1][6:9] + general_matrix[2][6:9]

	matrix4 = general_matrix[3][0:3] + general_matrix[4][0:3] + general_matrix[5][0:3]

	matrix5 = general_matrix[3][3:6] + general_matrix[4][3:6] + general_matrix[5][3:6]

	matrix6 = general_matrix[3][6:9] + general_matrix[4][6:9] + general_matrix[5][6:9]

	matrix7 = general_matrix[6][0:3] + general_matrix[7][0:3] + general_matrix[8][0:3]

	matrix8 = general_matrix[6][3:6] +general_matrix[7][3:6] + general_matrix[8][3:6]

	matrix9 = general_matrix[6][6:9] + general_matrix[7][6:9] + general_matrix[8][6:9]

	

	# Loading game board
	result = []
	result.append(matrix1)
	result.append(matrix2)
	result.append(matrix3)
	result.append(matrix4)
	result.append(matrix5)
	result.append(matrix6)
	result.append(matrix7)
	result.append(matrix8)
	result.append(matrix9)

	print (result)
	return result


load_test("SUDUKO_Input1.txt")