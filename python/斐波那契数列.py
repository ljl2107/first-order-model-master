# Fibonacci series
a = 1
b = 1
i = 1
print(a," ",b,end=" ")
while i < 10 :
    # c = a + b
    # print(c,end=" ")
    # a = b
    # b = c
    a, b= b,a + b
    print(b, end=" ")
    i += 1
