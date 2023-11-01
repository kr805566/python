from collections import OrderDict
import random
nums = []

for n in range(10):
    nums.append(random.randint(-100,100))
    nums.sort()
    od = OrderDict()  

for i in nums:
    if i not in od:
        od[i] = nums.count(i)

for k,v in od.items():
    if v > 1:
        print('number is {},count is {}'.format(k,v))
