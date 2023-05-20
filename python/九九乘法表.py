"""打印九九乘法表"""

i = 1

while i <= 9:
    j = 1
    while j <= i:
        print(i,"*",j,"=",i*j,end = " ")
        j = j + 1
    i = i + 1
    print("\n")
