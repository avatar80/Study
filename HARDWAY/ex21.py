# _*_ coding:utf-8 _*_

def add(a, b):
    print("덧셈 %d + %d"%(a,b))
    return a+b

def substract(a, b):
    print("뺄셈 %d - %d"%(a,b))
    return a-b

def multiply(a, b):
    print("곱셈 %d * %d"%(a,b))
    return a*b

def devide(a, b):
    print("나눗셈 %d * %d"%(a,b))
    return a/b

age = add(40,5)
hegiht = substract(87,6)
weight = multiply(90,2)
iq = devide(100,2)

print("A:%d B:%d C:%d D:%d"%(age,hegiht,weight,iq))
