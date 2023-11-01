# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 15:59:49 2019

@author: Hydra
"""

import random
count = 0
password = random.randint(1, 1000)

while count <3:
      count += 1
      x = int(input("請輸入密碼："))
      
      if x == password:
         print("正確")
         break
      elif count == 3:
         print("剩餘嘗試次數已用盡")
         break     
      else:
         print("錯誤")
         
     