import re;
rules = {
    "IF_TOKEN": "^if$",
    "WHILE_TOKEN": "^while$",
    "FOR_TOKEN": "^for$",
    "ID": "^[a-zA-Z]\w*$",
    "INTEGER": "^\-?[0-9]+$",
    "FLOAT": "^\-?[0-9]+\.[0-9]+$",
    "RELOP": "^((>|<|=)=|(>|<))$",
}


symbol_table = dict()

def lex(word):
    for token,expression in rules.items():
        regex = re.compile(expression)
        if regex.match(word):
            return token
    return "ERROR"

    
def analyze():
    file = open("input.dat",'r')
    for line in file.readlines():
        for lexeme in line.split(" "):
            print("Token:",lex(lexeme))
            print("Lexeme:",lexeme, end="\n\n")
    file.close()
    
analyze()
