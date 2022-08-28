import matplotlib.pyplot as plt
#function for LCG
def LCG(a,c,m,x,n):
  xlist=[]
  ylist=[]
  for i in range (n):
    x=((a*x)+c)%(m)
    xlist.append(x/m)
    ylist.append(i+1)
  plt.plot(ylist,xlist,'.')
  plt.show()
x1=LCG(1103515245,12345,32768,10,1000)