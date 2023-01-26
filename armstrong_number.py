for i in range(10001):
    num=i
    c=len(str(i))
    result=0
    while(i!=0):
        digit=i%10
        result=result+digit**c
        i=i//10
    if num==result:
        print(num)


