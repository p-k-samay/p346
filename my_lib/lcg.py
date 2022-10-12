def random(x,n):
    a=1103515245
    c=12345
    m=32768
    xlist=[]
    for i in range (0,n):
        x=(a*x+c)%m
        xlist.append(x/m)
    return xlist
        