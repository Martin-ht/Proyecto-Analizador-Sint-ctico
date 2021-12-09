
import sys
import ply.yacc as yacc
from ruby_resevadas import tokens

VERBOSE = 1

precedence = (
    ('left', 'COMMA'),
    ('left', 'EQUAL', 'PLUSEQUAL', 'MINUSEQUAL'),
    ('left', 'SEMI'),
    ('nonassoc', 'ISEQUAL', 'DEQUAL'),
    ('nonassoc', 'LESS', 'LESSEQUAL', 'GREATER', 'GREATEREQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('right', 'LBRACKET'),
    ('left', 'ELSIF'),
    ('left', 'ELSE'),
)

def p_program(p):
    '''program : contsDecl '''
    pass

def p_contsDecl(p):
    ''' contsDecl : contsDecl declaration 
                  | declaration'''
    pass

def p_declaration(p):
    '''declaration : str_declaration
                   | var_declaration
                   | iffor_declaration 
                   | comt_declaration
                   | def_declaration 
                   | end_declaration'''
    pass


def p_str_declaration(p):
    '''str_declaration : PUTS STRING
                       | PUTS VARIABLE
                       | PUTS VARIABLE PLUS VARIABLE'''
    pass

def p_var_declaration(o):
    '''var_declaration : VARIABLE EQUAL STRING
                       | VARIABLE EQUAL INT
                       | VARIABLE EQUAL VARIABLE
                       | VARIABLE EQUAL FLOAT
                       | VARIABLE EQUAL FLOAT PLUS FLOAT
                       | VARIABLE EQUAL INT PLUS INT
                       | VARIABLE EQUAL VARIABLE PLUS INT
                       | VARIABLE PLUS EQUAL INT
                       | VARIABLE PLUS EQUAL VARIABLE
                       | VARIABLE MINUS EQUAL INT'''
    pass

def p_iffor_declaration(p):
    '''iffor_declaration : IF VARIABLE ISEQUAL STRING str_declaration
                         | ELSE str_declaration
                         | ELSE
                         | IF VARIABLE LESSEQUAL STRING str_declaration 
                         | IF VARIABLE LESSEQUAL VARIABLE 
                         | IF VARIABLE LESSEQUAL STRING var_declaration str_declaration 
                         | IF VARIABLE LESSEQUAL STRING empty '''
    pass

def p_comt_declaration(p):
    '''comt_declaration : COMMENTS'''
    pass

def p_def_declaration(p):
    '''def_declaration : DEF VARIABLE LPAREN VARIABLE COMMA VARIABLE RPAREN str_declaration
                       | DEF VARIABLE LPAREN VARIABLE COMMA VARIABLE RPAREN str_declaration iffor_declaration
                       | VARIABLE LPAREN VARIABLE COMMA VARIABLE RPAREN '''
    pass

def p_end_declaration(p):
    '''end_declaration : END'''
    pass

def p_empty(p):
	'empty :'
	pass
    
def p_error(p):
    if VERBOSE:
        if p is not None:
            print (chr(27)+"[1;31m"+"\t ERROR: Syntax error - Unexpected token" + chr(27)+"[0m")
            #print ("\t\tLine: "+str(p.lexer.lineno)+"\t=> "+str(p.value))
            print ('\t|Error en la LINEA: [{:3}] Por => [{:20}] |'.format(p.lexer.lineno,p.value))
        else:
            print (chr(27)+"[1;31m"+"\t ERROR: Syntax error"+chr(27)+"[0m")
            print ("\t\tLine:  "+str(ruby_resevadas.lexer.lineno))

    else:
        raise Exception('syntax', 'error')

parser = yacc.yacc()

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        script = sys.argv[1]

        scriptfile = open(script, 'r')
        scriptdata = scriptfile.read()
        #print (scriptdata)

        print (chr(27)+"[0;36m"+"INICIA ANALISIS SINTACTICO"+chr(27)+"[0m")
        parser.parse(scriptdata, tracking=False)
        #print("No Tienes Errores Sintacticos En El Codigo Ruby")
        print (chr(27)+"[0;36m"+"TERMINA ANALISIS SINTACTICO"+chr(27)+"[0m")

    else:
        print (chr(27)+"[0;31m"+"Pase el archivo de script RB como parametro:")
        print (chr(27)+"[0;36m"+"\t$ python ProgramaRuby.py"+chr(27)+"[1;31m"+" <filename>.rb"+chr(27)+"[0m")