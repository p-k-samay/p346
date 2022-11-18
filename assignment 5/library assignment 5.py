import numpy as np
def lcg(a,c,x,m):    #Without plots
    r=[]
    d=[]
    for i in range(0,200):
        y=((a*x+c)%m)/m
        x=y
        r.append(i)
        d.append(y)
        # print(y)
    return d
def midpoint(f,a,b,N):
    h=(b-a)/N
    x=[]
    t=0
    for i in range(1,N+1):
        t=(a+(i-1)*h+a+i*h)/2
        x.append(t)
    sum=0
    for j in range(0,N):
        sum+=h*f(x[j])
    return "%.8f"%sum

def trapezoidal(f,a,b,n):
    h=(b-a)/n
    x=[]
    t=0
    for i in range(1,n+1):
        t=(a+(i-1)*h+a+i*h)/2
        x.append(t)
    sum=0

    for j in range(0,n):
        x_n=x[j]+h
        sum+=h*(f(x_n)+f(x[j]))/2
        x[j]=x_n
    return '%.8f'%sum

def simpson(f,a,b,n):
    h=(b-a)/n
    x=a 
    sum=0
    for i in range(n):
        sum+=(f(x)+4*f(x+h/2)+f(x+h))*h/6
        x+=h
    return '%.8f'%sum

def monte_carlo(f,a,b,n):
    sum1=0
    e=lcg(1103515245,12345,1,32768)
    F=0
    for i in range(n):
        X=a+(b-a)*e[i]
        sum1+=f(X)
    F=(b-a)*sum1/n
    return F

