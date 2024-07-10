import ply.lex as lex

#List of token names

tokens = (
    'LET', "IDENTIFIER", "EQUALS", "NUMBER", "PLUS", "MINUS", "TIMES", "DIVIDE", "LPAREN", "RPAREN", "SEMICOLON"
)

# Regular expression rules for simple tokens
t_LET = r'let'
t_EQUALS = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'



def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.vlaue = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

#Error handling rule

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

#Build the lexer
lexer = lex.lex()

#Test it out
if __name__ == "__main__":
    data = '''
    let x = 3;
    let y = 4;
    let z = x + y;
    '''
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)  # Print the token   