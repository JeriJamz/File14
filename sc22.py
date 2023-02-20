#####################
#CONSTANTS
#################

Digits = '0123456789'

###############
#ERROR
##########

class Error:
    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details
    
    def as_string(self):
        result = f'{self.error_name}: {self.details}'
        return result

class IllegalCharError(Error):
    def __init__(self, details):
        super().__init__('Illegal Char', details)
#########################
#tokens
####################

TT_INT = 'TT_INT'
TT_FLOAT = 'FLOAT'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'

class Token:
    def __init__(self, type, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

####################
#LEXER
##################

class Lexer:
    def __init__(self, txt):
        self.txt = txt
        self.pos = -1
        self.current_char = None
        self.adv = adv()
    
    def adv(self):
        self.pos += 1
        self.current_char = self.txt[self.pos] if self.pos < len(self.txt) else None

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in '\t':
                self.adv()
            elif self.current_char in Digits:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS))
                self.adv()
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS))
                self.adv()
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL))
                self.adv()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV))
                self.adv()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN))
                self.adv()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN))
                self.adv()
            else:#error
                char = self.current_charself.adv()
                return[], IllegalCharError("'" + char + "'")

        return tokens, None

    def make_number(self):
        num_str = ''
        dot_cnt = 0

    while self.current_char != None and self.current_char in Digits + '.':
        if self.current_char == '.':
            if dot_cnt == 1:break
            dot_cnt += 1
            num_str += '.'
        else:
            num_str += self.current_char
        self.adv()

    if dot_cnt == 0:       
        print(Token(TT_INT, int(num_str)))
    else:
        print(Token(TT_FLOAT, float(num_str)))

##############################
#RUN
########################

def run(txt):
    lexer = Lexer(txt)
    tokens, error = lexer.make_token()

    return tokens, error
