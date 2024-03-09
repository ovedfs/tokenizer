class Token:
	def __init__(self, kind, value, line, column):
		self.type = kind
		self.value = value
		self.line = line
		self.column = column

	def __repr__(self):
		return f"\n<{self.type}, {self.value}, {self.line}, {self.column}>"
	

class Integer(Token):
  def __init__(self, value, line, column):
    super().__init__('INT', value, line, column)
  

class Float(Token):
  def __init__(self, value, line, column):
    super().__init__('FLOAT', value, line, column)


class Operation(Token):
  def __init__(self, value, line, column):
    super().__init__('OP', value, line, column)
  

class Assign(Token):
  def __init__(self, line, column):
    super().__init__('ASSIGN', '=', line, column)


class Variable(Token):
  def __init__(self, value, line, column):
    super().__init__('VAR', value, line, column)