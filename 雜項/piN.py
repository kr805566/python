# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 15:54:21 2019

@author: Bird
"""

玩家輸入的值 = input('請輸入一個奇數n:'+'\n')#輸入值
玩家輸入的值=int(玩家輸入的值)
總和=0

i=1
正負=1;

while i<=玩家輸入的值:
    總和=總和 +正負*4/i
    正負=正負*-1
    i=i+2

print(總和)
    
    