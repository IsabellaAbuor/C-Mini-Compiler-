from sly import Parser
from LexicalAnalyzer import CalcLexer

class CalcParser(Parser):
    tokens = CalcLexer.tokens #getting the token list from the lexer

    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/'),
        ('left', '.'),
        )

    def __init__(self, variables: dict = None):
        self.variables = variables or {}
        self.stack = []

    @property
    def last_item_on_stack(self):
        return self.stack[-1] if len(self.stack) > 0 else None

    @_('arithmaticOperation')
    def expression(self, p):
        pass

    @_('literal') # This must be added to avoid infinite recursion
    def expression(self, p):
        pass

    @_('literal PLUS expression') # The operation is between a literal and another expression to allow chaining operators
    def arithmaticOperation(self, p):
        value2, value1 = self.stack.pop(), self.stack.pop()  # The order of pop is inverted to the insertion
        try:
            self.stack.append(value1 + value2)  # Could be string or numbers
        except TypeError:
            self.stack.append(None)

    @_('literal MINUS expression')
    def arithmaticOperation(self, p):
        value2, value1 = self.stack.pop(), self.stack.pop()
        try:
            self.stack.append(value1 - value2)  # Can only be numbers
        except TypeError:
            self.stack.append(None)

    @_('literal TIMES expression')
    def arithmaticOperation(self, p):
        value2, value1 = self.stack.pop(), self.stack.pop()  # The order of pop is inverted to the insertion
        try:
            self.stack.append(value1 * value2)  # Could be string or numbers
        except TypeError:
            self.stack.append(None)

    @_('literal DIVIDE expression')
    def arithmaticOperation(self, p):
        value2, value1 = self.stack.pop(), self.stack.pop()  # The order of pop is inverted to the insertion
        try:
            self.stack.append(value1 / value2)  # Can only be numbers
        except TypeError:
            self.stack.append(None)

    @_('NUMBER',
       'NUMBER "." NUMBER',
       'STRING')  # Notice how we apply a number of grammar rules to the same method

    @_('IDENTIFIER')
    def literal(self, p):
        self.stack.append(self.variables.get(p[0], 0))

if __name__ == '__main__':
    lexer = CalcLexer()
    parser = CalcParser()
    
    while True:
        try:
            text = input(calc > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            print(tree)
