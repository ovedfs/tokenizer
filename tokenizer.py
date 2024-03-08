import sys
import re
from lib.Token import Token

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
					# Integers
					if line[i] in '0123456789':
						number = ''
						column = i
						while line[i] in '0123456789' and i < len(line):
							number += line[i]
							i += 1
						Program.tokens.append(Token('INT', number, num_line, column))
					# Operators
					elif line[i] in '+-*/':
						Program.tokens.append(Token('OP', line[i], num_line, i))
					# Assign operator
					elif line[i] == '=':
						Program.tokens.append(Token('ASSIGN', '=', num_line, i))
					# Variables
					elif re.match(r'[a-z_]', line[i]):
						name = line[i]
						column = i
						i += 1
						while re.match(r'[a-z0-9_]', line[i]) and i < len(line):
							name += line[i]
							i += 1
						Program.tokens.append(Token('VAR', name, num_line, column))
					
					i += 1

code = sys.argv[1]

program = Program(code)

try:
	program.tokenize()
except Exception as e:
	print(e)

print(program.tokens)
