#basic
import sys,time

def delay_print(c):
    for s in c:
        sys.stdout.write(s)
        sys.stdout.flush()
        time.sleep(0.005)

##############################
#*******CONSTANTS
##############################

DIGITS = '0123456789'

##############################
#****ERRORS
##############################

class Error:
    def __init__(self,pos_start, pos_end,error_name,details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f"{self.error_name}: {self.details}"
        result += f'File {self.pos_start.fn}, line{self.pos_start.ln + 1}'
        return result

class IllegelCharError(Error):
    def __init__(self, pos_start, pos_end, error_name, details):
        super().__init__(pos_start, pos_end,'Illegal Characters', details)

############################
#********Posistions**********
############################

class Position():
    def __init__(self, idx, ln, col, fn, ftxt):
        self.idx = idx
        self.ln = ln 
        self.col = col
        self.fn = fn 
        self.ftxt = ftxt

    def adv(self, current_char):
        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1
            self.col = 0
        
        return self

    def copy(self):
        return Position(self.idx,  self.ln, self.col, self.fn, self.ftxt)
#############################
# ****TOKEN******
#############################

TT_INT = 'TT_INT'
TT_FLOAT = 'FLOAT'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL' 
TT_DIV = 'DIV'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'
TT_BOOLEAN = 'BOOLEAN'



class Token:
    def __init__(self, type_,value = None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

        #this gives token a representive so when the token called on it'll print the type and then
        #the value and if it doesnt have a value itll print the type instead

##############################
### ********Lexer
#############################

class Lexer:
    def __init__(self,fn,text):
        self.fn = fn
        self.text = text
        self.pos = Position(-1, 0, -1, fn, text)
        self.current_char = None
        self.adv()

    def adv(self):
        self.pos.adv(self.current_char)
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in ' \t':
                self.adv() 
            elif self.current_char in DIGITS:
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
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.adv()
                return[], IllegelCharError(pos_start, self.pos,"'" + char + "'")

        return tokens, None

def make_number(self):
    num_str = ''
    dot_count = 0

    while self.current_char != None and self.current_char in DIGITS + '.':
        if self.current_char == '.':
            if dot_count == 1: break
            dot_count += 1
            num_str += 1
        else:
            num_str += self.current_char
        self.adv()

    if dot_count == 0:
        return Token(TT_INT, int(num_str))
    else:
        return Token(TT_FLOAT, float(num_str))



################################
#* RUN
################################

def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()

    return tokens, error

delay_print('My First attempt at writing a program.\n(name is still top secrect.)\n')
delay_print('For now the program can use basic math operators.\n')
delay_print('|###      <<<...Still Under Construction###Caution>>>      ####\n')