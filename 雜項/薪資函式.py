def 薪資(工時):
    獎金 = 0
    時薪 = 150
    基本薪水 = 0
    if 工時 >= 100:
        n=工時 /100
        獎金 += 1000 *n
    基本薪水 = 工時 * 時薪
    總薪資 = 基本薪水 + 獎金
    return 總薪資

姓名 = str(input("請輸入你的姓名:"))
n = int(input("請輸入你的工時:"))
x = 薪資(n)
print(姓名,x)
