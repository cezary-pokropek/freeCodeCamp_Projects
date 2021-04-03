def arithmetic_arranger(problems, solve_problem=False):

	if len(problems) > 5:
		return "Error: Too many problems."
	else:
		top_line = ''
		middle_line = ''
		dashes_line = ''
		answer_line = ''
		longest_digit = 0
		problem_count = 0

		# ==> Iterates through each of the problem, splits each problem in into sections of a question
		for problem in problems:
			problem_split = problem.split(' ')

			# ==> Assigns a meaningful name to the extracted section from the problem - 'top_number', 'operator', 'bottom_number'
			top_number = problem_split[0]
			operator = problem_split[1]
			bottom_number = problem_split[2]

			# ==> Creates a list of valid operator signs used in the problems, will be used to determine if an invalid operator has been used.
			sign_operator_list = ['+', '-']

			# ==> Compares and determines which of the problem numbers have the longer digits - top or bottom number, then assigns to a variable 'longest_digit'
			top_num_len = len(top_number)
			btm_num_len = len(bottom_number)
			if top_num_len > btm_num_len:
				longest_digit = top_num_len
			elif top_num_len < btm_num_len:
				longest_digit = btm_num_len
			elif top_num_len == btm_num_len:
				longest_digit = top_num_len

			if top_num_len > 4 or btm_num_len > 4:
				return "Error: Numbers cannot be more than four digits."

			if operator not in sign_operator_list:
				return "Error: Operator must be '+' or '-'."

			if not top_number.isdigit() or not bottom_number.isdigit():
				return "Error: Numbers must only contain digits."

			# ==> Determines the type of operator and performs the calculations - Addtion if '+' / Subtraction if '-'.
			if operator == '+':
				answer = int(top_number) + int(bottom_number)
			if operator == '-':
				answer = int(top_number) - int(bottom_number)

			# ==> Creates a variable that represents 'longest_digit' length plus '2', for the single space between the operator and the longest of the two numbers.
			spanner = longest_digit + 2

			# ==> Assigns the formatted values from the extracted section after the '.split()' to the variables representing question section/structure/answer.
			top_line += top_number.rjust(spanner)
			middle_line += operator + bottom_number.rjust(spanner - 1) 
			dashes_line += '-' * spanner
			answer_line += str(answer).rjust(spanner)       

			# ==> Creates a variable containing 4 spaces.
			blank_space = '    '

			# ==> Adds to the problem counter and determines if there are still questions in the problems, 
			#     adds 'blank_space' to the end of each question section/structure/answer - four spaces between each problem.
			problem_count += 1
			if problem_count < len(problems):
				top_line += blank_space
				middle_line += blank_space
				dashes_line += blank_space
				answer_line += blank_space

				# ==> Cleans/Strips each question section/structure/answer row of unwanted characters
				top_line.rstrip()
				middle_line.rstrip()
				dashes_line.rstrip()
				answer_line.rstrip()

		# ==> Determines if the function was invoked/called with the second argument 'solve_problem' has been set to 'True', if so
		#     calculation results/answer performed will be displayed on output/return, if not, only the question will be shown.
		if solve_problem:
			arranged_problems = top_line + '\n' + middle_line + '\n' +  dashes_line + '\n' + answer_line
		else:
			arranged_problems = top_line + '\n' + middle_line + '\n' + dashes_line
		return arranged_problems

