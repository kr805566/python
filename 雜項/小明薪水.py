# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 22:43:17 2019

@author: Bird
"""

小明目前月薪=28000
小明目前年薪=小明目前月薪*12

小明月薪加倍=56000

幾年=0

while 小明目前月薪<= 小明月薪加倍 :
    小明目前年薪=小明目前年薪*1.03
    小明目前月薪=小明目前年薪/12
    幾年=幾年+1
    
print (幾年)
