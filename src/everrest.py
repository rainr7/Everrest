from sys import *
import re
from lexer import lex
from everrest_parser import parse

# tokens = []
# num_stack = []
# symbols = {}


def open_file(filename):
    if(".evr" in filename):
        data = open(filename, "r").read()
        data += "<EOF>"
        return data
    else:
        print("Tidak merupakan everrest file, pastikan ekstensi file .evr")
        exit()


def run():
    data = open_file(argv[1])
    toks = lex(data)
    parse(toks)


run()