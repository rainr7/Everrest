import re

class Lexer(object):

    def __init__(self, source_code):
        self.source_code = source_code
    
    def tokenize(self):
        
        tokens = []

        source_code = self.source_code.split()
        source_index = 0

        while source_index < len(source_code):
            kata = source_code[source_index]
            
            if kata == "var":
                tokens.append(["DEKLARASI_VAR", kata])
            elif kata == "print":
                tokens.append(["DEKLARASI_PRINT", kata])    
            elif re.match('[a-z]', kata) or re.match('[A-Z]', kata):
                if kata[len(kata)-1] == ";":
                    tokens.append(["MODIFIER", kata[0:len(kata)-1]])
                else:
                    tokens.append(["MODIFIER", kata])

            elif re.match('[1-9]', kata):
                if kata[len(kata)-1] == ";":
                    tokens.append(["INTEGER", kata[0:len(kata)-1]])
                else:                    
                    tokens.append(["INTEGER", kata])
                    
            elif kata in "+-/*":
                if kata[len(kata)-1] == ";":
                    tokens.append(["OPERATOR", kata[0:len(kata)-1]])
                tokens.append(["OPERATOR", kata])

            if kata[len(kata)-1] == ";":
                tokens.append(["AKHIR_STATEMENT", ";"])
            source_index += 1
        print(tokens)


