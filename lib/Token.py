class Token:
	def __init__(self, kind, value, line, column):
		self.type = kind
		self.value = value
		self.line = line
		self.column = column

	def __repr__(self):
		return f"\n<{self.type}, {self.value}, {self.line}, {self.column}>"