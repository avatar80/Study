# _*_ coding:utf-8 _*_

from sys import argv

script, user_name = argv
prompt = '> '

print("안녕 %s, 나는 %s 스크립트야"%(user_name, script))
print("몇가지 질문을 할께.")
print("%s, 나를 좋아해? "%user_name)
likes = input(prompt)

print("%s, 어디에 살아? "%user_name)
lives = input(prompt)

print("%s, 무슨 컴퓨터를 가지고 있어? "%user_name)
computer = input(prompt)

print("""
좋아, 나를 좋아하냐는 질문에는 '%s',
'%s'에 살아. 어디인진 모르겠지만,
그리고 '%s' 컴퓨터를 가졌어, 멋져.
"""%(likes, lives, computer))
