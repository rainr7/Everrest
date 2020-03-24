def main():

	content = ""
	with open('test.ev', 'r') as file:
		content = file.read()
		print(content)

main()