from interpt import evaluationExpr
from interpt import evalExpr
from interpt import doPrint
from interpt import doAssign
from interpt import doSambung
from interpt import getInput
from interpt import getVariabel

num_stack = []
symbols = {}


def parse(toks):
    i = 0
    length = len(toks)
    while(i < len(toks)):
        if toks[i] == "SELESAI":
            i += 1
        elif toks[i] == "KALAUTIDAK":
            return 0
        elif toks[i] + " " + toks[i+1][0:6] == "PRINT STRING" or toks[i] + " " + toks[i+1][0:3] == "PRINT NUM" or toks[i] + " " + toks[i+1][0:4] == "PRINT EXPR" or toks[i] + " " + toks[i+1][0:3] == "PRINT VAR":
            if toks[i+1][0:6] == "STRING":
                doPrint(toks[i+1], 0)
            elif toks[i+1][0:3] == "NUM":
                doPrint(toks[i+1], 0)
            elif toks[i+1][0:4] == "EXPR":
                doPrint(toks[i+1], 0)
            elif toks[i+1][0:3] == "VAR":
                doPrint(getVariabel(toks[i+1]), 0)
            i += 2
        elif toks[i] + " " + toks[i+1][0:6] == "SAMBUNG STRING" or toks[i] + " " + toks[i+1][0:3] == "SAMBUNG NUM" or toks[i] + " " + toks[i+1][0:4] == "SAMBUNG EXPR" or toks[i] + " " + toks[i+1][0:3] == "SAMBUNG VAR":
            if toks[i+1][0:6] == "STRING":
                doSambung(toks[i+1])
            elif toks[i+1][0:3] == "NUM":
                doSambung(toks[i+1])
            elif toks[i+1][0:4] == "EXPR":
                doSambung(toks[i+1])
            elif toks[i+1][0:3] == "VAR":
                doSambung(getVariabel(toks[i+1]))
            i += 2
        elif toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:6] == "VAR EQUALS STRING" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:3] == "VAR EQUALS NUM" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:4] == "VAR EQUALS EXPR" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:3] == "VAR EQUALS VAR":
            if toks[i+2][0:6] == "STRING":
                doAssign(toks[i], toks[i+2])
            elif toks[i+2][0:3] == "NUM":
                doAssign(toks[i], toks[i+2])
            elif toks[i+2][0:4] == "EXPR":
                doAssign(toks[i], "NUM:" + str(evaluationExpr(toks[i+2][5:])))
            elif toks[i+2][0:3] == "VAR":
                doAssign(toks[i], getVariabel(toks[i+2]))
            i += 3
        elif toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2][0:3] == "MASUKAN STRING VAR":
            getInput(toks[i+1][7:], toks[i+2][4:])
            i += 3
        elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] + " " + toks[i+4] == "JIKA NUM EQEQ NUM MAKA":

            if toks[i+1][4:] == toks[i+3][4:]:
                i += 5
            elif "KALAUTIDAK" in toks:
                kalautidakPos = toks.index('KALAUTIDAK')
                i += kalautidakPos + 1
            # else:
            #     return 0

        elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] + " " + toks[i+4] == "JIKA NUM GREATEQUALS NUM MAKA":

            if toks[i+1][4:] >= toks[i+3][4:]:
                i += 5
            elif "KALAUTIDAK" in toks:
                kalautidakPos = toks.index('KALAUTIDAK')
                i += kalautidakPos + 1
            # else:
            #     return 0

        elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] + " " + toks[i+4] == "JIKA NUM LOWEQUALS NUM MAKA":

            if toks[i+1][4:] <= toks[i+3][4:]:
                i += 5
            elif "KALAUTIDAK" in toks:
                kalautidakPos = toks.index('KALAUTIDAK')
                i += kalautidakPos + 1
            # else:
            #     return 0
        elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] + " " + toks[i+4] == "JIKA NUM LOW NUM MAKA":

            if toks[i+1][4:] < toks[i+3][4:]:
                i += 5
            elif "KALAUTIDAK" in toks:
                kalautidakPos = toks.index('KALAUTIDAK')
                i += kalautidakPos + 1
            # else:
            #     return 0
        elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] + " " + toks[i+4] == "JIKA NUM GREATHER NUM MAKA":

            if toks[i+1][4:] > toks[i+3][4:]:
                i += 5
            elif "KALAUTIDAK" in toks:
                kalautidakPos = toks.index('KALAUTIDAK')
                i += kalautidakPos + 1
            # else:
            #     return 0
        elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] == "UNTUK NUM SAMPAI NUM":

            awal = int(toks[i+1][4:])
            akhir = int(toks[i+3][4:])

            for x in range(awal, akhir):
                if toks[i+5][0:6] == "STRING":
                    doPrint(toks[i+5], 0)
                elif toks[i+5][0:3] == "NUM":
                    doPrint(toks[i+5], 0)
                elif toks[i+5][0:4] == "EXPR":
                    doPrint(toks[i+5], 0)
                elif toks[i+5][0:3] == "VAR":
                    doPrint(getVariabel(toks[i+5]), 0)
            i += 6
