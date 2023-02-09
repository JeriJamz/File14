class Lexer:
    def __init__(self,input): 
        self.source = input + '\n'
        self.curChar = ''
        self.curPos = -1
        self.nextChar()
        

    #process the next character
    def nextChar(self):
        self.curPos += 1
        if self.curPos >= len(self.source):
            self.curChar = '\0' #eof(pray for me)
        else:
            self.curChar = self.source[self.curPos]
        

    #return the lookahead character
    def peek(self):
        if self.curPos + 1 >= len(self.source):
            return '\0'
        return self.source[self.curPos+1]
        

    #invalid token found, print error message and exit
    def abort(self,message):
        pass

    #skip whitespaces except newlines, gone use to identfy the end of a statment
    def skipWhitespace(self):
        pass

    #skip comments in the code
    def skipComment(self):
        pass

    #return the next token
    def getToken(self):
        pass
