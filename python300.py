''''
#87 환율 계산기
def calExchangeRate():
    dicEx = { "dollor":1167, "yen":1.096, "euro":1268, "wyen":171 }

    strInput = input("입력:")
    val = strInput.strip().split(" ")
    nEx = int(dicEx[val[1]])
    nResult = int(val[0]) * nEx
    print("%.3f won"%(nResult))
'''

'''
#90 대소문자 변환
def TransUpperLower():
    strInput = input("입력 :")
    if strInput.isupper() == True :
        print(strInput.lower())
    else:
        print(strInput.upper())
'''

'''
#92 in 연산자
def warningInvest():
    warn_investment_list = ["Nicrosoft", "Doogle", "Never", "KiKio", "SEMSUNG", "HELG"]

    strItem = input("종목:")
    if strItem in warn_investment_list :
        print("투자경고 종목입니다.")
    else:
        print("투자경고 종목이 아닙니다.")
'''

#93 남여 구분하기
'''
def findGender():
    regisNumber = input("주민등록번호:")
    listRegisNum = regisNumber.split('-')
    strNum = listRegisNum[1]
    if ('1' or '3') in strNum[0]:
        print("Men")
    else:
        print("Women")
'''

#findGender() #93
#warningInvest() #92
#TransUpperLower() #90
#calExchangeRate() #87










