#this is SF


######################
#* CONSTANTS
#######################

Digits = '0123456789'

#########################
#* ERROR
#########################

class Error(self):k



########################
#*** Tokens
########################

# Token const
TT_INT = 'INT'
TT_FLOAT = 'FLOAT'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'
TT_BOOLEAN  = 'BOOLEAN'

class Tokens:
    def __init__(self, type, value):
        self.type = type
        self.value =  value

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'


###########################
# ***LEXER
###########################

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.adv()

    def adv(self):
        self.pos += 1
        self.current_char = self.text[pos] if self.pos < len(self.text) else None

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in '\t':
                self.adv()
            elif self.current_char in Digits:
                tokens.append(self.make_numbers())
            elif self.current_char == '+':
                tokens.append(tokens(TT_PLUS))
                self.adv()
            elif self.current_char == '-':
                tokens.append(tokens(TT_MINUS))
                self.adv()
            elif self.current_char == '*':
                tokens.append(tokens(TT_MUL))
                self.adv()
            elif self.current_char == '/':
                tokens.append(tokens(TT_DIV))
                self.adv()
            elif self.current_char == '(':
                tokens.append(tokens(TT_LPAREN))
                self.adv()
            elif self.current_char == ')':
                tokens.append(tokens(TT_RPAREN))
                self.adv()
            else:
                #return sometype of error

        return tokens



def make_number(self):
    num_str  = ''
    dot_count = 0

    while self.current_char != None and self.current_char in Digits + '.':
        if self.current_char == '.':
            if dot.count == 1: break
            dot_count += 1
            num_str += '.'
        else:
            num_str += self.current_char


    if dot_count == 0:
        return Tokens(TT_INT, int(num_str))
    else:
        return Tokens(TT_FLOAT, float(num_str))
