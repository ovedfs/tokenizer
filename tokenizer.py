import sys
import re
from lib.Tokens import Token, Integer, Float, Operation, Assign, Variable

class Program:
	tokens = []

	def __init__(self, code):
		self.code = code

	def __repr__(self):
		return "\n".join([repr(item) for item in Token.tokens]) or ""

	def tokenize(self):
		with open(self.code, 'r') as file:
			for num_line, line in enumerate(file):
				i = 0
				while i < len(line):
					# Numbers
					if line[i] in '0123456789':
						number = ''
						isFloat = False
						column = i
						while line[i] in '0123456789.' and i < len(line):
							if line[i] == '.':
								isFloat = True
							number += line[i]
							i += 1

						if isFloat is False:
							Program.tokens.append(Integer(number, num_line, column)) 
						else:
							Program.tokens.append(Float(number, num_line, column))
					# Operators
					elif line[i] in '+-*/':
						Program.tokens.append(Operation(line[i], num_line, i))
					# Assign operator
					elif line[i] == '=':
						Program.tokens.append(Assign(num_line, i))
					# Variables
					elif re.match(r'[a-z_]', line[i]):
						name = line[i]
						column = i
						i += 1
						while re.match(r'[a-z0-9_]', line[i]) and i < len(line):
							name += line[i]
							i += 1
						Program.tokens.append(Variable(name, num_line, column))
					
					i += 1

code = sys.argv[1]

program = Program(code)

try:
	program.tokenize()
	print(program.tokens)
except Exception as e:
	print(e)
