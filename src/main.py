import lexer

def main():

	content = ""
	with open('test.evr', 'r') as file:
		content = file.read()


	lex = lexer.Lexer(content)
	lex.tokenize()

main()