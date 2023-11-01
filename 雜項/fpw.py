# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 22:13:49 2019

@author: Bird
"""
from random import randint


最低值 = 1
最高值 = 100
答案值 = randint(最低值, 最高值)


while True: #無限迴圈
    
    玩家輸入的值 = input('請輸入 '+str(最低值) + '到' + str(最高值)+'\n')#輸入值
    玩家輸入的值 = int(玩家輸入的值)

    if 玩家輸入的值 <= 最低值 or 玩家輸入的值 >= 最高值:#判斷是否在範圍內
        print('請輸入 ' + str(最低值) + '-' + str(最高值) + ' 之間\n')
        continue
    
    if 玩家輸入的值 == 答案值:
        print('答對了！')
        break   #答對跳迴圈
    elif 玩家輸入的值 < 答案值:
        最低值 = 玩家輸入的值
    elif 玩家輸入的值 > 答案值:
        最高值 = 玩家輸入的值