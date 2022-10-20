import math
def newton_raphson(x_0):
    x = x_0
    x_old = x + 1
    iter_count = 0
    iter_limit=100
    ϵ=10 ** -4
    while abs(x_old - x) > ϵ:
        x_old = x
        x = x - (f(x) / df(x))
       
    return x
def f(x):
  return(x-5)*(math.exp(x))+5
def df(x):
  return(x-5)*(math.exp(x))+5
x = newton_raphson(5)
h = 6.626* 10**(-34)
k = 1.381* 10**(-23)
c = 3* 10**8
b = h*c/(x*k)
print(b)


