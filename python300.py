




'''
#87 환율 계산기
def calExchangeRate():
    dicEx = { "dollor":1167, "yen":1.096, "euro":1268, "wyen":171 }

    strInput = input("입력:")
    val = strInput.strip().split(" ")
    nEx = int(dicEx[val[1]])
    nResult = int(val[0]) * nEx
    print("%.3f won"%(nResult))
'''


#calExchangeRate() #87










