#this is the source code
########################
#CONSTANTS
########################
Digits = '0123456789'

#######################
#ERRORS
#######################

class Error:
    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details
    
    def as_string(self):
        result = f'{self.error_name}: {self.details}'#should return the error name: details
        return result

class IllegalCharError(Error):
    def __init__(self, details):
        super().__init__('Illegal Character', details)

########################
# POSITION
########################

#########################
# TOKENS
##########################
#* Constants for TOKENS
# TT stands for token type


TT_INT = 'TT_INT'#0123456789
TT_FLOAT = 'FLOAT'#.00001
TT_PLUS = 'PLUS'# + 
TT_MINUS = 'MINUS'# - 
TT_MUL = 'MUL'# * 
TT_DIV = 'DIV'# / 
TT_LPAREN = 'LPAREN'# ( 
TT_RPAREN = 'RPAREN'# )


class Tokens:
    def __init__(self,type_,value = None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'#if token has a value it will print the 'type:value'
        return f'{self.type}'#if it doesnt have a value it will print jus the type

############################
#LEXER
############################

class Lexer:#this is what read the text
    def __init__(self,text):
        self.text = text #this makes text and obj of lexer
        self.pos = -1#make sure it doesnt start at a blank space and the code starts to freak out
        self.current_char = None#agains sets everything basically to 0 or -1
        self.adv()

    def adv(self):
        self.pos += 1
        #below is where the lexer will advance but what stops it from being an infinite loop is the else None
        # current char is linked with adv. and is equal to the pos of the text. 
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None 

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in '\n':#this will check for blank spaces and move on
                self.adv()
            elif self.current_char in Digits:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Tokens(TT_PLUS))#i might have to call it tokens(remember to add the S)
                self.adv()
            elif self.current_char == '-':
                tokens.append(Tokens(TT_MINUS))
                self.adv()
            elif self.current_char == '*':
                tokens.append(Tokens(TT_MUL))
                self.adv()
            elif self.current_char == '/':
                tokens.append(Tokens(TT_DIV))
                self.adv()
            elif self.current_char == '(':
                tokens.append(Tokens(TT_LPAREN))
                self.adv()
            elif self.current_char == ')':
                tokens.append(Tokens(TT_RPAREN))
                self.adv()
            else:
                char = self.current_char
                self.adv()
                return [], IllegalCharError("' " + char +" '")

        return tokens, None


    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char != None and self.current_char in Digits + '.':
            if self.current_char == '.':
                if dot_count == 1: break 
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
                self.adv()
            
        if dot_count == 0:
            return Tokens(TT_INT, int(num_str))
        else:
            return Tokens(TT_FLOAT, float(num_str))

    
############################
#Run
############################

def run(text):
    lexer = Lexer(text)
    tokens, error =  lexer.make_tokens()   

    return tokens, error