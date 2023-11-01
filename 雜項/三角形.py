# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a=int(input("輸入A?"))
b=int(input("輸入B?"))
c3=int(input("輸入C?"))


if a+b>c and b+c>a and a+c>b:
    if a==b and b==c:
        print("正三角形")
    elif a==b or b==c or a==c:
        print("等腰三角形")
    else: 
        print("一般三角形")
else:
    print("不是三角形")
